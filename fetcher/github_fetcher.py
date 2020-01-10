import os
from github import Github

# using username and password
GITHUB_PERSONAL_ACCESS_TOKEN = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]


class GithubFetcherCollaborators:
    def __init__(self):
        self.github = Github(GITHUB_PERSONAL_ACCESS_TOKEN)

    def get_collaborators_created_at(self, owner_name, repo_name):
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
