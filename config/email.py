from modules.core.config import *


class Email:

    # Return the SMTP credentials
    @staticmethod
    def get():
        return config['SMTP']

