#!/usr/bin/python3
"""  Using REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and export data in JSON format.
"""
import requests
import json
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_url(id):
    """ Export information from an API about
        `TODO` list progress to JSON file
    """
    user_url = f"{url}/users/{id}"
    username = ""
    with requests.get(user_url) as resp:
        username = resp.json()['username']

    todo_url = f"{url}/todos?userId={id}"
    with requests.get(todo_url) as resp:
        myList = resp.json()
        newDict = {}
        with open(f"{id}.json", "w", encoding="UTF-8") as f:
            newList = []
            for j in myList:
                myDict = {}
                myDict["task"] = j["title"]
                myDict["completed"] = j["completed"]
                myDict["username"] = username
                newList.append(myDict)
            newDict[id] = newList
            json.dump(newDict, f)


if __name__ == "__main__":
    fetch_url(argv[1])
