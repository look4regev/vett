import os
from github import Github

GITHUB_URL_PREFIX = "https://github.com/"


class GithubFetcherCollaborators:
    def __init__(self):
        github_personal_access_token = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]
        self.github = Github(github_personal_access_token)

    def get_collaborators_created_at(self, url):
        owner_name, repo_name = parse_github_url(url)
        user = self.github.get_user(owner_name)
        repository = user.get_repo(repo_name)
        collaborators = repository.get_collaborators()
        pushable_collaborators = [
            coll for coll in collaborators if coll.permissions.push
        ]
        pushable_collaborators_created_at = {
            collaborator.login: collaborator.created_at
            for collaborator in pushable_collaborators
        }
        return pushable_collaborators_created_at


def parse_github_url(url):
    last_slash_index = url.rfind("/")
    owner = url[len(GITHUB_URL_PREFIX) : last_slash_index]
    repo = url[last_slash_index + 1 :]
    return owner, repo
