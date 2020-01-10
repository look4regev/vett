import sys

from fetcher.github_fetcher import GithubFetcherCollaborators
from grading.collaborators_grader import CollaboratorsGrader


def main():
    fetcher = GithubFetcherCollaborators()
    grader = CollaboratorsGrader(fetcher)
    result, failed = grader.grade_collaborators_veterancy("look4regev", "vett")
    if result:
        print("All good")
        return 0
    else:
        print(f"Suspicious! {failed}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
