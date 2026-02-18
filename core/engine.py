import random
from core.packet import Packet
from core.event_bus import EventBus
from core.constants import *
from core.state_machine import TCPState
from simulation.transport import Transport

class ProtocolEngine:
    def __init__(self):
        self.bus = EventBus()
        self.transport = Transport(self.receive)

        self.client_state = TCPState.CLOSED
        self.server_state = TCPState.LISTEN

        self.client_seq = random.randint(100, 500)

    def start(self):
        self.bus.emit("client_state", self.client_state)
        self.bus.emit("server_state", self.server_state)

    def connect(self):
        pkt = Packet(SYN, self.client_seq, None, CLIENT, SERVER)
        self.client_state = TCPState.SYN_SENT
        self.bus.emit("client_state", self.client_state)
        self._send(pkt)

    def send_data(self, msg):
        if self.client_state != TCPState.ESTABLISHED:
            self.connect()
            return

        pkt = Packet(DATA, self.client_seq, None, CLIENT, SERVER, msg)
        self._send(pkt)

    def _send(self, pkt):
        self.bus.emit("packet_sent", pkt)
        self.transport.send(pkt)

    def receive(self, pkt):
        self.bus.emit("packet_received", pkt)

        if pkt.pkt_type == SYN:
            self.server_state = TCPState.SYN_RECEIVED
            self.bus.emit("server_state", self.server_state)

            reply = Packet(SYN_ACK, 999, pkt.seq + 1, SERVER, CLIENT)
            self._send(reply)

        elif pkt.pkt_type == SYN_ACK:
            self.client_state = TCPState.ESTABLISHED
            self.bus.emit("client_state", self.client_state)

            ack = Packet(ACK, pkt.ack, pkt.seq + 1, CLIENT, SERVER)
            self._send(ack)

        elif pkt.pkt_type == ACK:
            self.server_state = TCPState.ESTABLISHED
            self.bus.emit("server_state", self.server_state)

        elif pkt.pkt_type == DATA:
            self.bus.emit("message", pkt.payload)
