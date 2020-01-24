#!/usr/bin/env python3

from modules.github.authenticate import Authenticate
from modules.core.git import Git
from config.metadata import Metadata
from modules.core.file import File
from modules.core.boot import Boot
from config.threads import Threads
from functools import partial
from multiprocessing import Pool

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


class Pullit:

    # Pullit constructor
    def __init__(self):
        self.auth = Authenticate().get()

    # Find credentials
    @staticmethod
    def find(repo):
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

        # Delete the repo
        Git.delete(repo.full_name)

    # Run pullit
    def main(self):
        # Pool connections to speed up our job
        with Pool(processes=Threads.get()) as pool:
            while True:
                function = partial(self.find)
                pool.map(function, list(self.auth.get_repos()[:Threads.get()]))


# Pullit logo
print(logo)

# Boot method (LEAVE ALONE)
Boot()

# Let's go!
Pullit().main()

