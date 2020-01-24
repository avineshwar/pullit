import sys, glob
from modules.github.authenticate import Authenticate
from modules.core.git import Git
from config.metadata import Metadata
logo = f"""
{'#' * 60}
#                                                          #
# Pullit: Created by @Filtration                           #
#                                                          #
# I take no responsibility for what you do with this tool  #
# It is more than likely illegal to use in your country    #
#                                                          #

{'#' * 60}
"""
print(logo)


a = Authenticate().get()

for repo in a.get_repos():

    Metadata.get()

    Git.clone(repo.full_name, "https://github.com/%s.git" % repo.full_name)

    for file in glob.glob("/tmp/pullit/git/%s/*.txt" % repo.full_name, recursive=True):
        print(file)

    sys.exit(1)