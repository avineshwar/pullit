import os


class Slack:

    # Return the slack token
    @staticmethod
    def token():
        return os.getenv('SLACK_API')

