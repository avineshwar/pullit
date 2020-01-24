class Events:

    # Listeners subscribed
    subscribers = {}

    # Events constructor
    def __init__(self):
        pass

    # Listen for event
    @staticmethod
    def listen(self, name, handler):
        self.subscribers[name] = handler

    # Emit an event
    @staticmethod
    def emit(self, name, payload):
        self.subscribers[name](payload)

