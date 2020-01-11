import os
from github import Github

GITHUB_URL_PREFIX = "https://github.com/"
SCANNED_COMMITS_COUNT = 30


class GithubFetcherCollaborators:
    def __init__(self):
        github_personal_access_token = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]
        self.github = Github(github_personal_access_token)

    def get_latest_collaborators_created_at(self, url):
        owner_name, repo_name = parse_github_url(url)
        user = self.github.get_user(owner_name)
        repository = user.get_repo(repo_name)
        commits = repository.get_commits()
        pushable_collaborators_created_at = {}
        for i in range(SCANNED_COMMITS_COUNT):
            committer = commits[i].committer
            pushable_collaborators_created_at[committer] = committer.created_at
        return pushable_collaborators_created_at


def parse_github_url(url):
    last_slash_index = url.rfind("/")
    owner = url[len(GITHUB_URL_PREFIX) : last_slash_index]
    repo = url[last_slash_index + 1 :]
    return owner, repo
