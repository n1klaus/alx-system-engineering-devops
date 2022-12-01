#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    case-insensitive, delimited by spaces
"""
from collections import OrderedDict
import requests

url = "https://www.reddit.com"


def recurse(subreddit: str, word_list: list, page=None):
    """
    Args:
        subreddit: subreddit
        word_list: list of keywords to search for
        page: identifier for the current page to work on

    Returns:
        count of occurences of each keywords in hot posts
        if the subreddit is valid,
        otherwise None

    """
    next_page = "?after={}".format(page) if page else ""
    endpoint = "/r/{0}/hot/.json{1}".format(subreddit, next_page)
    json_data = ""
    counter = dict(zip(word_list, [0 for i in range(len(word_list))]))
    if subreddit:
        try:
            full_url = "{0}{1}".format(url, endpoint)
            headers = {"User-Agent": "100-count"}
            resp = requests.get(full_url, headers=headers)
            json_data = resp.json()
            new_page = json_data.get('data').get('after')
            children = json_data.get('data').get('children')
            if children and subreddit == children[0].get(
                    'data').get('subreddit'):
                for child in children:
                    title = child.get('data').get('title')
                    for word in word_list:
                        if str.count(str.lower(title), str.lower(word)):
                            counter[word] = counter[word] + \
                                str.count(str.lower(title), str.lower(word))
                if new_page:
                    new_counter = recurse(subreddit, word_list, new_page)
                    if new_counter:
                        for key, value in new_counter.items():
                            counter[key] += value
                return counter
        except BaseException:
            pass
    return None


def count_words(subreddit: str, word_list: list):
    """
    Args:
        subreddit: subreddit
        word_list: list of keywords to search for

    Returns:
        count of occurences of each keywords in hot posts
        if the subreddit is valid,
        otherwise None

    """
    final_counter = {}
    word_counter = recurse(subreddit, word_list)
    if word_counter:
        for key, value in word_counter.items():
            if str.lower(key.strip()) in final_counter:
                value += final_counter[str.lower(key.strip())]
            if value != 0:
                final_counter[str.lower(key.strip())] = value
        result = dict(sorted(final_counter.items(),
                             key=lambda tup: (tup[1], tup[0])))
        for key, value in result.items():
            print("{0}: {1}".format(key, value))
        return final_counter
    return None
