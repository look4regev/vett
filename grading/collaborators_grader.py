from datetime import datetime, timedelta

DAYS_IN_YEAR = 365
VETERANCY_THRESHOLD_DAYS = 2 * DAYS_IN_YEAR


class CollaboratorsGrader:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def grade_collaborators_veterancy(self, owner, repo):
        collaborators_created_at = self.fetcher.get_collaborators_created_at(
            owner, repo
        )
        younger_than_threshold = [
            collaborator.login
            for collaborator, created_at in collaborators_created_at.items()
            if created_at + timedelta(days=VETERANCY_THRESHOLD_DAYS) > datetime.now()
        ]
        return not bool(younger_than_threshold), younger_than_threshold
