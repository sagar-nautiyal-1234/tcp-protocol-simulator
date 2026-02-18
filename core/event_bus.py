class EventBus:
    def __init__(self):
        self.listeners={}

    def subscribe(self,event,func):
        self.listeners.setdefault(event,[]).append(func)

    def emit(self,event,data=None):
        for f in self.listeners.get(event,[]):
            f(data)
