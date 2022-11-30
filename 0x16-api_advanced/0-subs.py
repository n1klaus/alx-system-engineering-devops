#!/usr/bin/python3

"""
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
"""
import requests

url = "https://www.reddit.com"


def number_of_subscribers(subreddit: str):
    """
    Args:
        subreddit: subreddit

    Returns:
        number of subscribers if the subreddit is valid,
        otherwise 0

    """
    endpoint = "/r/{}.json?limit=1".format(subreddit)
    json_data = ""
    count = 0
    if len(subreddit) > 0:
        try:
            full_url = "{0}{1}".format(url, endpoint)
            headers = {"User-Agent": "0-subs"}
            resp = requests.get(full_url, headers=headers)
            json_data = resp.json()
            count = json_data.get('data').get('children')[0].get(
                    'data').get('subreddit_subscribers')
        except BaseException:
            pass
    return count
