from modules.github.authenticate import Authenticate


a = Authenticate("71a9df1cda228fd86a5511ab9afdde62509922a9").get()

for repo in a.get_repos():
    print(repo.name)