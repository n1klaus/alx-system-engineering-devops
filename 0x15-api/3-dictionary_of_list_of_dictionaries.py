#!/usr/bin/python3
"""  Using REST API, for all employees,
    returns information about their TODO list progress
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
    with requests.get(f"{url}/users") as resp:
        users = resp.json()
    print(users)
    for user in users:
        print(user.id)
        with requests.get(f"{url}/users/{user.id}") as resp:
            username = resp.json()['username']
        print(username)
        todo_url = f"{url}/todos?userId={user.id}"
        with requests.get(todo_url) as resp:
            myList = resp.json()
            newDict = {}
            with open("todo_all_employees.json", "w", encoding="UTF-8") as f:
                newList = []
                for j in myList:
                    myDict = {}
                    myDict["username"] = username
                    myDict["task"] = j["title"]
                    myDict["completed"] = j["completed"]
                    newList.append(myDict)
                newDict[id] = newList
                json.dump(newDict, f)


if __name__ == "__main__":
    fetch_url(argv[1])
