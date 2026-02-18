import threading,time

class Transport:
    def __init__(self,deliver):
        self.deliver=deliver

    def send(self,pkt):
        def run():
            time.sleep(0.6)
            self.deliver(pkt)
        threading.Thread(target=run,daemon=True).start()
