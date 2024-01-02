#!/usr/bin/python3
"""
script to export data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":
    USERS = []
    TASKS = []
    DATA = dict()
    URL = "http://jsonplaceholder.typicode.com"
    filename = "todo_all_employees.json"
    users = requests.get("{}/users".format(URL)).json()
    todos = requests.get("{}/todos".format(URL)).json()
    for u in users:
        USERS.append((u.get('id'), u.get('username')))
    for t in todos:
        TASKS.append((t.get('userId'),
                      t.get('title'),
                      t.get('completed')))
    for user in USERS:
        todo = []
        user = list(user)
        for task in TASKS:
            task =list(task)
            if task[0] == user[0]:
                todo.append({
                        "username": user[1],
                        "task": task[1],
                        "completed": task[2]
                        })
        DATA[str(user[0])] = todo
    with open(filename, "w") as jsonfile:
        json.dump(DATA, jsonfile, sort_keys=True)
