#!/usr/bin/python3
"""
1. Top Ten.
"""

import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit.
    """
    URL = "https://www.reddit.com/r/{}//hot.json?limit=10".format(subreddit)
    response = requests.get(URL,
                            headers={"User-Agent": "user_agent_00"},
                            allow_redirects=False)
    ten_posts = response.json().get('data', {}).get('children', [])
    if not ten_posts:
        print(None)
    for post in ten_posts:
        title = post.get('data').get('title')
        print(title)
