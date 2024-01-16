#!/usr/bin/python3
""" Script that contains the functon that retrieves the number of
    a subscribers of a subreddit using Reddit API.
"""
from requests import get


def number_of_subscribers(subreddit):
    """ Retrieves the number of subscribers of a subreddit
        using the Reddit API.
        Args:
            @subreddit: the subreddit to get the count from
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "0x16. API advanced by Cu7ious"}

    response = get(url, headers=headers).json()
    return response.get('data', {}).get('subscribers', 0)
