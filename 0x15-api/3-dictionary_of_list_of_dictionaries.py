#!/usr/bin/python3
"""  Using REST API, for all employees,
    returns information about their TODO list progress
    and export data in JSON format.
"""
import requests
import json
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_all():
    """ Export information from an API about
        `TODO` list progress to JSON file
    """
    newDict = {}
    for user in requests.get(f"{url}/users").json():
        with requests.get(f"{url}/users/{user.get('id')}") as resp:
            username = resp.json()['username']
        todo_url = f"{url}/todos?userId={user.get('id')}"
        with requests.get(todo_url) as resp:
            myList = resp.json()
            newList = []
            for j in myList:
                myDict = {}
                myDict["username"] = username
                myDict["task"] = j["title"]
                myDict["completed"] = j["completed"]
                newList.append(myDict)
            newDict[user.get('id')] = newList
    with open("todo_all_employees.json", "w", encoding="UTF-8") as f:
        json.dump(newDict, f)


if __name__ == "__main__":
    fetch_all()
