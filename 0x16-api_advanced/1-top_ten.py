#!/usr/bin/python3

"""
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
"""
import requests

url = "https://www.reddit.com"


def top_ten(subreddit: str):
    """
    Args:
        subreddit: subreddit

    Returns:
        titles of the top ten posts if the subreddit is valid,
        otherwise None

    """
    endpoint = "/r/{}/top/.json?t=day&limit=10".format(subreddit)
    json_data = ""
    if len(subreddit) > 0:
        try:
            full_url = "{0}{1}".format(url, endpoint)
            headers = {"User-Agent": "1-top_ten"}
            with requests.get(full_url, headers=headers) as resp:
                json_data = resp.json()
                children = json_data.get('data').get('children')
                data = children[0].get('data')
                if data and subreddit == data.get('subreddit'):
                    titles = []
                    for child in children:
                        titles.append(child.get('data').get('title'))
        except BaseException:
            raise
    if titles:
        for title in titles:
            print(title)
    else:
        print(None)
