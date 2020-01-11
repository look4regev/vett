import pytest

from fetcher.github_fetcher import parse_github_url


@pytest.mark.parametrize(
    "url,expected",
    [("https://github.com/someowner/somerepo", ("someowner", "somerepo"))],
)
def test_parse_github_url(url, expected):
    assert parse_github_url(url) == expected
