from modules.core.config import *


class Metadata:

    # Return a list of metadata
    @staticmethod
    def get():
        return config['METADATA']

