from dataclasses import dataclass,field
from datetime import datetime

@dataclass
class Packet:
    pkt_type:str
    seq:int
    ack:int|None
    sender:str
    receiver:str
    payload:str|None=None
    time:datetime=field(default_factory=datetime.now)
    retries:int=0

    def __str__(self):
        return f"{self.pkt_type} {self.sender}->{self.receiver} seq={self.seq} ack={self.ack} r={self.retries}"
