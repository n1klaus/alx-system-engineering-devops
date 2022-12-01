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
        count: iterator for all posts in response

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
#            print(full_url)
            headers = {"User-Agent": "2-recurse"}
            resp = requests.get(full_url, headers=headers)
            json_data = resp.json()
            page = json_data.get('data').get('after')
            children = json_data.get('data').get('children')
            if children and subreddit == children[0].get('data').get('subreddit'):
                for child in children:
                    titles.append(child.get('data').get('title'))
                if page:
                    new_titles = recurse(subreddit, hot_list, page)
                    if new_titles:
                        titles.extend(list(new_titles))
        except BaseException:
            raise
    if titles:
        return titles
    else:
        return None
