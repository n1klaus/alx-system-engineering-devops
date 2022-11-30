#!/usr/bin/python3
"""
    Using REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and export data in JSON format.
"""
import json
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_url(id):
    """
    Args:
        id: id of the user
    Returns:
        information from an API about
        `TODO` list progress to export to JSON file
    """
    user_url = "{0}/users/{1}".format(url, id)
    username = ""
    resp = requests.get(user_url)
    username = resp.json()['username']

    todo_url = "{0}/todos?userId={1}".format(url, id)
    resp = requests.get(todo_url)
    myList = resp.json()
    newDict = {}
    with open("{}.json".format(id), "w", encoding="UTF-8") as f:
        newList = []
        for j in myList:
            myDict = {}
            myDict["task"] = str(j["title"])
            myDict["completed"] = j["completed"]
            myDict["username"] = str(username)
            newList.append(myDict)
        newDict[id] = newList
        json.dump(newDict, f)


if __name__ == "__main__":
    fetch_url(argv[1])
