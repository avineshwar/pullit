import sys, glob
from modules.github.authenticate import Authenticate
from modules.core.git import Git
from config.metadata import Metadata
from modules.core.file import File

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

    # Clone the repo
    Git.clone(repo.full_name, "https://github.com/%s.git" % repo.full_name)

    # Run the metadata on the repo
    # todo: move each type in to own function in file class
    for metadata in Metadata.get():
        if metadata['type'] == 'contents':
            print('match regex for all files')
        elif metadata['type'] == 'extension':
            File(repo).find_by_extension(metadata['match'])
        elif metadata['type'] == 'filename':
            File(repo).find_by_name(metadata['match'])

    sys.exit(1)