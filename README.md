# Pullit

Pullit is a real-time credential finder. 

<img src="https://i.imgur.com/yartJ8d.png">

### Installation

- ``` git pull https://github.com/filtration/pullit.git ```
- ``` sudo chmod +x install.sh  ```
- ``` . ./install.sh ```
- ``` python ./pullit.py  ```


### Modules:

- Github
- Bitbucket (todo)
- Gitlab (todo)


### todo:


- Check rate limiting
- Slack notifications
- Email notifications
- Save to sqlite file for example: <br>
    1. repos:
        - id
        - repo_name (name of the repo)
        - scanned_at (when we last scanned it)
        - commit_id (id of the commit so we don't scan again)
    2. credentials:
        - id
        - repo_id (repo we scanned and found creds)
        - match (what metadata was used)
        - name (name of the metadata)
        - credentials (json object of the credentials/location)
- more metadata to search for
- maybe if credentials are found, keep a local copy of the repo???