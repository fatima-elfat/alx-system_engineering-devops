#!/usr/bin/python3
"""
2. Recurse it!
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit.
        If no results are found for the given subreddit,
        the function should return None.

    Args:
        subreddit (str): the name of the subreddit.
        hot_list (list, optional): hot list. Defaults to [].
        after (str, optional): value of the last post in page.
    """
    URL = "https://www.reddit.com/r/{}//hot.json".format(subreddit)
    if after != "":
        URL = URL + "?after={}".format(after)
    response = requests.get(URL,
                            headers={"User-Agent": "user_agent_00"},
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    rs = response.json().get('data', {}).get('children', [])
    a = response.json().get('data', {}).get('after')
    for r in rs:
        hot_list.append(r.get('data').get('title'))
    if not a:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=a)
