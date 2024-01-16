#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0#!/usr/bin/python3
""" How many subs? """


def number_of_subscribers(subreddit):
    """ Returns subscriber count of subreddit or 0 """
    from requests import get

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    try:
        js = r.json()

    except ValueError:
        return 0

    data = js.get("data")

    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count

    return 0
