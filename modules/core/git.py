import os


class Git:

    # Clone a git repo
    @staticmethod
    def clone(name, url):
        os.system("git clone --single-branch --no-tags --depth 1 %s /tmp/pullit/git/%s" % (url, name))

    # Delete the repo
    def delete(self, name):
        pass

