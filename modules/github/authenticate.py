from github import Github


class Authenticate:

    # Authenticate constructor
    def __init__(self, token):
        self.github = Github(token)

    # Get the authenticate object
    def get(self):
        return self.github

