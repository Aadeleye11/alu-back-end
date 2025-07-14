#!/usr/bin/python3
"""
Fetch and display TODO list progress of a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    emp_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(emp_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task))


