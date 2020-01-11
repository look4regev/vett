#!/usr/bin/env python
import sys
import argparse

from fetcher.github_fetcher import GithubFetcherCollaborators
from grading.collaborators_grader import CollaboratorsGrader


def main():
    parser = argparse.ArgumentParser(description="Github repo scanner")
    parser.add_argument("-u", "--url", required=True)
    args = parser.parse_args()
    fetcher = GithubFetcherCollaborators()
    grader = CollaboratorsGrader(fetcher)
    result, failed = grader.grade_collaborators_veterancy(args.url)
    if result:
        print("All good")
        return 0
    else:
        print(f"Suspicious! {failed}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
