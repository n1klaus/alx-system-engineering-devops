#!/usr/bin/python3
"""
    Using REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and export data in CSV format.
"""
from csv import writer
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
        `TODO` list progress for export to csv file
    """
    user_url = "{0}/users/{1}".format(url, id)
    username = ""
    resp = requests.get(user_url)
    username = resp.json()["username"]

    todo_url = "{0}/todos?userId={1}".format(url, id)
    resp = requests.get(todo_url)
    myList = resp.json()

    with open("{}.csv".format(id), "w", encoding="UTF-8") as f:
        w = writer(f)
        for j in myList:
            newList = []
            newList.extend(
                          (
                           "{}".format(j["userId"]),
                           "{}".format(username),
                           "{}".format(j["completed"]),
                           "{}".format(j["title"])
                          )
                          )
            w.writerow(newList)


if __name__ == "__main__":
    fetch_url(argv[1])
