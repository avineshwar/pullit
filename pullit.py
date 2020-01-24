from modules.github.authenticate import Authenticate
from modules.core.git import Git
from config.metadata import Metadata
from modules.core.file import File
from modules.core.boot import Boot

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


class Pullit:

    # Pullit constructor
    def __init__(self):
        self.auth = Authenticate().get()

    # Run pullit
    def main(self):

        # Loop through repos and find matches
        for repo in self.auth.get_repos():

            # Clone the repo
            Git.clone(repo.full_name, "https://github.com/%s.git" % repo.full_name)

            # Run the metadata on the repo
            for metadata in Metadata.get():
                if metadata['type'] == 'contents':
                    File(repo).find_by_content(metadata['match'])
                elif metadata['type'] == 'extension':
                    File(repo).find_by_extension(metadata['match'])
                elif metadata['type'] == 'filename':
                    File(repo).find_by_name(metadata['match'])


pullit = Pullit()
pullit.main()
