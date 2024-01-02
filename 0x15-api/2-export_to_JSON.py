#!/usr/bin/python3
"""
export data in the JSON format.
Records all tasks that are owned by this employee
Format must be: { "USER_ID":
[{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"},
... ]}
File name must be: USER_ID.json
"""

from sys import argv
import requests
import json


if __name__ == "__main__":
    URL = "http://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(URL, argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(URL, argv[1])).json()
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as jsonfile:
        tlist = []
        USERNAME = user.get("username")
        for t in todos:
            taskdict = {"task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": USERNAME}
            tlist.append(taskdict)
        data = {str(argv[1]): tlist}
        json.dump(data, jsonfile)
