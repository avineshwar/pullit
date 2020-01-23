import os


class Github:

    # Github config constructor
    @staticmethod
    def tokens():
        t = list(os.getenv('GITHUB_TOKENS'))
        print(t)
        return os.getenv('GITHUB_TOKENS')

