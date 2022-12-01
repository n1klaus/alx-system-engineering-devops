#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
"""
import requests

url = "https://www.reddit.com"


def recurse(subreddit: str, hot_list: list = [], count=0):
    """
    Args:
        subreddit: subreddit
        hot_list: list of titles of hot posts
        count: iterator for all posts in response

    Returns:
        list of titles of the all hot posts if the subreddit is valid,
        otherwise None

    """
    endpoint = "/r/{}/hot/.json".format(subreddit)
    json_data = ""
    titles = []
    if subreddit:
        try:
            full_url = "{0}{1}".format(url, endpoint)
            headers = {"User-Agent": "2-recurse"}
            resp = requests.get(full_url, headers=headers)
            json_data = resp.json()
            children = json_data.get('data').get('children')
            data = children[count].get('data')
            if data and subreddit == data.get('subreddit'):
                titles.extend(children[count].get('data').get('title'))
                count += 1
                if children[count]:
                    new_titles = recurse(subreddit, hot_list, count)
                    if new_titles:
                        titles.extend(new_titles)
        except BaseException:
            pass
    if titles and titles not in hot_list:
        hot_list.extend(titles)
        return hot_list
    else:
        return None
