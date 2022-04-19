__all__ = [
    'github', 'push_issue'
]

from github import Github

def github(access_key, repository_name):
    g = Github(access_key)
    repo = g.get_user().get_repo(repository_name)
    return repo


def push_issue(repo, title, body):
    repo.create_issue(title=title, body=body)
