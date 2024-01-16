#!/usr/bin/python3
"""
3. Count it!
"""

import requests


def count_words(subreddit, word_list, after="", saved={}):
    """_summary_

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
    for r in rs:
        t = r.get('data').get('title').lower()
        for w in word_list:
            if w.lower() in t:
                c = 0
                for i in t.split():
                    if i == w.lower():
                        c = c + 1
                if saved.get(w) is None:
                    saved[w] = c
                else:
                    saved[w] = c + saved[w]
    if not a:
        if len(saved) != 0:
            saved = sorted(saved.items(), key=lambda it: it[1], reverse=True)
            for key, val in saved:
                print("{}: {}".format(key, val))
        print("")
        return
    count_words(subreddit, word_list, after=a, saved=saved)
