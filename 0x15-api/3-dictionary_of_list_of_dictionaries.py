#!/usr/bin/python3
"""
    Using REST API, for all employees,
    returns information about their TODO list progress
    and export data in JSON format.
"""
import json
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com"


def fetch_all():
    """
        Export information from an API about
        `TODO` list progress to JSON file
    """
    newDict = {}
    for user in requests.get("{}/users".format(url)).json():
        resp = requests.get("{0}/users/{1}".format(url, user.get("id")))
        username = resp.json()['username']
        todo_url = "{0}/todos?userId={1}".format(url, user.get("id"))
        resp = requests.get(todo_url)
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
