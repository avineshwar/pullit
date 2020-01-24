from modules.core.config import *


class Slack:

    # Return the slack token
    @staticmethod
    def token():
        return config['SLACK_API']

