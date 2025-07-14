#!/usr/bin/python3
"""
Fetches and displays the TODO list progress of a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    name = user.get("name")
    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task))


