import modules.core.boot
from modules.github.authenticate import Authenticate

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


l = ["223"]
print(l[0])
a = Authenticate().get()

for repo in a.get_repos():
    print(repo.name)