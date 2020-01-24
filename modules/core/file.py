import glob


class File:

    # File constructor
    def __init__(self, repo):
        self.repo = repo

    # Find a file by its extension
    def find_by_extension(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/*%s" % (self.repo.full_name, match), recursive=True):
            print(file)

    # Find a file by its name
    def find_by_name(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/%s" % (self.repo.full_name, match), recursive=True):
            print(file)

