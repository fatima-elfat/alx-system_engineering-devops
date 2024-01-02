#!/usr/bin/python3
"""
script to export data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":
    URL = "http://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(URL)).json()
    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        tlist = []
        datas = {}
        for user in users:
            USERNAME = user.get("username")
            USERID = user.get("id")
            todos = requests.get("{}/todos?userId={}".format(
                                                            URL,
                                                            USERID
                                                            )).json()
            for task in todos:
                data = {"username": USERNAME,
                        "task": task.get("title"),
                        "completed": task.get("completed")
                        }
                tlist.append(data)
            datas[USERID] = tlist
        json.dump(datas, jsonfile)
