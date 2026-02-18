import random,threading
from core.packet import Packet
from core.event_bus import EventBus
from core.constants import *
from core.state_machine import TCPState
from simulation.transport import Transport

TIMEOUT=2

class ProtocolEngine:
    def __init__(self):
        self.bus=EventBus()
        self.transport=Transport(self.receive)

        self.client_state=TCPState.CLOSED
        self.server_state=TCPState.LISTEN

        self.client_seq=random.randint(100,400)
        self.server_seq=random.randint(700,1000)

        self.window_size=3
        self.in_flight=0
        self.waiting_ack=None

    def start(self):
        self.bus.emit("client_state",self.client_state)
        self.bus.emit("server_state",self.server_state)

    def connect(self):
        pkt=Packet(SYN,self.client_seq,None,CLIENT,SERVER)
        self.client_state=TCPState.SYN_SENT
        self.bus.emit("client_state",self.client_state)
        self._send_timeout(pkt)

    def send_data(self,msg):
        if self.client_state!=TCPState.ESTABLISHED:
            self.connect()
            return

        if self.in_flight>=self.window_size:
            self.bus.emit("window_full",None)
            return

        pkt=Packet(DATA,self.client_seq,None,CLIENT,SERVER,msg)
        self.client_seq+=1
        self.in_flight+=1
        self._send_timeout(pkt)

    def close(self):
        pkt=Packet(FIN,self.client_seq,None,CLIENT,SERVER)
        self.client_state="FIN_WAIT"
        self.bus.emit("client_state",self.client_state)
        self._send_timeout(pkt)

    def _send(self,p):
        self.bus.emit("packet_sent",p)
        self.transport.send(p)

    def _send_timeout(self,p):
        self.waiting_ack=p
        self._send(p)

        def timer():
            threading.Event().wait(TIMEOUT)
            if self.waiting_ack==p:
                p.retries+=1
                self.bus.emit("timeout",p)
                self._send_timeout(p)

        threading.Thread(target=timer,daemon=True).start()

    def receive(self,p):
        self.bus.emit("packet_received",p)

        if p.pkt_type==SYN:
            self.server_state=TCPState.SYN_RECEIVED
            self.bus.emit("server_state",self.server_state)
            reply=Packet(SYN_ACK,self.server_seq,p.seq+1,SERVER,CLIENT)
            self._send(reply)

        elif p.pkt_type==SYN_ACK:
            self.client_state=TCPState.ESTABLISHED
            self.bus.emit("client_state",self.client_state)
            ack=Packet(ACK,p.ack,p.seq+1,CLIENT,SERVER)
            self.waiting_ack=None
            self._send(ack)

        elif p.pkt_type==ACK:
            self.server_state=TCPState.ESTABLISHED
            self.bus.emit("server_state",self.server_state)
            self.waiting_ack=None
            if self.in_flight>0:
                self.in_flight-=1

        elif p.pkt_type==DATA:
            self.bus.emit("message",p.payload)
            ack=Packet(ACK,self.server_seq,p.seq+1,SERVER,CLIENT)
            self._send(ack)

        elif p.pkt_type==FIN:
            self.server_state="CLOSE_WAIT"
            self.bus.emit("server_state",self.server_state)
            ack=Packet(FIN_ACK,self.server_seq,p.seq+1,SERVER,CLIENT)
            self._send(ack)

        elif p.pkt_type==FIN_ACK:
            self.client_state="CLOSED"
            self.bus.emit("client_state",self.client_state)
            self.waiting_ack=None
