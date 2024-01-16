#!/usr/bin/python3
"""
0. How many subs?
"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): the name of the subreddit.
    """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(URL,
                            headers={"User-Agent": "user_agent_00"},
                            allow_redirects=False)
    subscribers = response.json().get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
