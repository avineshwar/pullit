from modules.core.events import Events


class Notifications:

    # Notifications constructor
    def __init__(self):
        Events.listen(Events, 'regex-found', self.slack)
        Events.listen(Events, 'extension-found', self.slack)
        Events.listen(Events, 'filename-found', self.slack)

    # Send information to slack
    def slack(self, payload):
        pass
        #print("Sent to slack", payload)

