#!/usr/bin/python3
"""
Exports TODO list data for a given employee ID to a CSV file.
"""

import csv
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

    filename = "{}.csv".format(emp_id)
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
