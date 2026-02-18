from dataclasses import dataclass
from datetime import datetime

@dataclass
class Packet:
    pkt_type: str
    seq: int
    ack: int | None
    sender: str
    receiver: str
    payload: str | None = None
    time: datetime = datetime.now()

    def __str__(self):
        return f"{self.pkt_type} | {self.sender}->{self.receiver} seq={self.seq} ack={self.ack}"
