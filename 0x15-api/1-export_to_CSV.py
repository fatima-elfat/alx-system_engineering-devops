#!/usr/bin/python3
"""
export data in the CSV format.
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    URL = "http://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(URL, argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(URL, argv[1])).json()
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        USERNAME = user.get("username")
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                                                    argv[1],
                                                    USERNAME,
                                                    task.get("completed"),
                                                    task.get("title")))
