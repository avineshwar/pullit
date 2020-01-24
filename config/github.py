from modules.core.config import *


class Github:

    # Github config constructor
    @staticmethod
    def tokens():
        return config['GITHUB_TOKENS'][0]

