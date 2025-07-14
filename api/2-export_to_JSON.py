#!/usr/bin/python3
"""
Exports all tasks of an employee to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos?userId={}".format(base_url, emp_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    data = []
    for task in todos:
        data.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    output = {emp_id: data}

    filename = "{}.json".format(emp_id)
    with open(filename, mode="w") as jsonfile:
        json.dump(output, jsonfile)
