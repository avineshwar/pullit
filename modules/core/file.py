import glob, re
from modules.core.events import Events


class File:

    # File constructor
    def __init__(self, repo):
        self.repo = repo

    # Find a file by its content
    def find_by_content(self, pattern):
        for file in glob.glob("/tmp/pullit/git/%s/**/*.*" % self.repo.full_name, recursive=True):
            try:
                with open(file) as f:
                    try:
                        for line in f:
                            for found in re.finditer(pattern, line):
                                information = "File: %s contains: %s" % (file, found.string)
                                print(information)
                                Events.emit(Events, 'regex-found', information)
                    except UnicodeDecodeError:
                        return
            except IsADirectoryError:
                return

    # Find a file by its extension
    def find_by_extension(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/*%s" % (self.repo.full_name, match), recursive=True):
            information = "Repo: %s contains: %s" % (self.repo.full_name, file)
            print(information)
            Events.emit(Events, 'extension-found', information)

    # Find a file by its name
    def find_by_name(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/%s" % (self.repo.full_name, match), recursive=True):
            information = "Repo: %s contains: %s" % (self.repo.full_name, file)
            print(information)
            Events.emit(Events, 'filename-found', information)

