#!/usr/bin/python3
"""  Using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_url(id):
    user_url = f"{url}/users/{id}"
    name = ""
    with requests.get(user_url) as resp:
        json = resp.json()
        name = json['name']

    todo_url = f"{url}/todos?userId={id}"
    with requests.get(todo_url) as resp:
        json = resp.json()
        f = filter(lambda x: True if x['completed'] is True else False, json)
        counter = 0
        titles = "\n"
        for i in f:
            counter += 1
            titles += f"\t{i['title']}\n"
        print(f"Employee {name} is done with tasks \
            ({counter}/{len(json)}): {titles[:-1]}")


if __name__ == "__main__":
    fetch_url(argv[1])
