#!/usr/bin/python3
"""  Using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_url(id):
    """ Return information from an API about
        TODO list progress
    """
    user_url = f"{url}/users/{id}"
    name = ""
    with requests.get(user_url) as resp:
        name = resp.json()['name']

    todo_url = f"{url}/todos?userId={id}"
    with requests.get(todo_url) as resp:
        json = resp.json()
        fl = filter(lambda x: True if x['completed'] is True else False, json)
        counter = 0
        titles = ""
        for item in fl:
            counter += 1
            titles += f"\t{item['title']}\n"
        print("Employee {0} is done with tasks ({1}/{2}):\n{3}".
              format(name, counter, len(json), titles[:-1]))


if __name__ == "__main__":
    fetch_url(argv[1])
