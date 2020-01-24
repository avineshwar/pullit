import os


class Git:

    # Clone a git repo
    @staticmethod
    def clone(name, url):
        os.system("git clone --single-branch --no-tags --depth 1 %s /tmp/pullit/git/%s > /dev/null 2>&1" % (url, name))

    # Delete the repo
    @staticmethod
    def delete(name):
        os.system("rm -rf /tmp/pullit/git/%s > /dev/null 2>&1" % name)

