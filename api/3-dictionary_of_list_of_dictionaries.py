#!/usr/bin/python3
"""
Exports all tasks from all employees to a JSON file
as a dictionary of lists of dictionaries.
"""

import json
import requests


def fetch_all_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def fetch_todos_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def main():
    users = fetch_all_users()
    all_data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = fetch_todos_by_user(user_id)

        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })
        all_data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)


if __name__ == "__main__":
    main()
