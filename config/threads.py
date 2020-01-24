from modules.core.config import *


class Threads:

    # Return amount of threads to use
    @staticmethod
    def get():
        return config['THREADS']

