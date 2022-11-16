#!/usr/bin/python3
"""  Using REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and export data in CSV format.
"""
from csv import writer
import json
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_url(id):
    """ Export information from an API about
        `TODO` list progress to csv file
    """
    user_url = f"{url}/users/{id}"
    username = ""
    with requests.get(user_url) as resp:
        username = resp.json()["username"]

    todo_url = f"{url}/todos?userId={id}"
    with requests.get(todo_url) as resp:
        myList = resp.json()

        with open(f"{id}.csv", "w", encoding="UTF-8") as f:
            w = writer(f)
            for j in myList:
                newList = []
                newList.extend(
                    (str(j['userId']), str(username), str(j['completed']),
                     str(j['title'])))
                print(newList)
                w.writerow(newList)


if __name__ == "__main__":
    fetch_url(argv[1])
