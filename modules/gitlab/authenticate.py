from github import Github
from config.github import Github as Config


class Authenticate:

    # Authenticate constructor
    def __init__(self):
        self.github = Github(Config.tokens())

    # Get the authenticate object
    def get(self):
        return self.github

