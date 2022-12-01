#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
"""
import requests

url = "https://www.reddit.com"


def recurse(subreddit: str, hot_list: list = [], page=None):
    """
    Args:
        subreddit: subreddit
        hot_list: list of titles of hot posts
        page: identifier for the current page to work on

    Returns:
        list of titles of the all hot posts if the subreddit is valid,
        otherwise None

    """
    next_page = "?after={}".format(page) if page else ""
    endpoint = "/r/{0}/hot/.json{1}".format(subreddit, next_page)
    json_data = ""
    titles = []
    if subreddit:
        try:
            full_url = "{0}{1}".format(url, endpoint)
            headers = {"User-Agent": "2-recurse"}
            resp = requests.get(full_url, headers=headers)
            json_data = resp.json()
            new_page = json_data.get('data').get('after')
            children = json_data.get('data').get('children')
            if children and subreddit == children[0].get(
                    'data').get('subreddit'):
                for child in children:
                    titles.append(child.get('data').get('title'))
                hot_list.extend(titles)
                if new_page:
                    new_titles = recurse(subreddit, hot_list, new_page)
                    if new_titles:
                        return new_titles
                return hot_list
        except BaseException:
            pass
    return None
