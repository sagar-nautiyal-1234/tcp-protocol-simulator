import threading
import time

class Transport:
    def __init__(self, deliver_callback):
        self.deliver = deliver_callback

    def send(self, packet):
        def delayed():
            time.sleep(0.6)
            self.deliver(packet)
        threading.Thread(target=delayed, daemon=True).start()
