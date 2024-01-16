#!/usr/bin/python3
"""
3. Count it!
"""

import requests


def count_words(subreddit, word_list, after="", saved={}):
    """ queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).

    Args:
        subreddit (str): the name of the subreddit.
        word_list (list): the list of word t search.
        after (str, optional): _description_. Defaults to "".
        saved (dict, optional): _description_. Defaults to {}.
    """
    URL = "https://www.reddit.com/r/{}//hot.json".format(subreddit)
    if after != "":
        URL = URL + "?after={}".format(after)
    response = requests.get(URL,
                            headers={"User-Agent": "user_agent_00"},
                            allow_redirects=False)
    if response.status_code != 200:
        print("")
        return
    rs = response.json().get('data', {}).get('children', [])
    a = response.json().get('data', {}).get('after')
    if rs is None:
        print("")
        return
    for r in rs:
        t = r.get('data').get('title').lower()
        for w in word_list:
            if w.lower() in t:
                cl = []
                for i in t.split():
                    if i == w.lower():
                        cl.append(i)
                    c = len(cl)
                if saved.get(w.lower()) is None:
                    saved[w.lower()] = c
                else:
                    saved[w.lower()] = c + saved[w.lower()]
    if a is None:
        if len(saved) != 0:
            saved = sorted(saved.items(), key=lambda it: (-it[1], it[0]))
            for key, val in saved:
                if val != 0:
                    print("{}: {}".format(key, val))
        print("")
        return
    return count_words(subreddit, word_list, after=a, saved=saved)
