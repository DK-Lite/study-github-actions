
import os
import re
from package import github, push_issue
from datetime import date



def main():
    access_key = os.environ['MY_GITHUB_TOKEN']
    repo = github(access_key, 'study-github-actions')
    push_issue(repo, 'a', "test")


if __name__ == "__main__":
    main()