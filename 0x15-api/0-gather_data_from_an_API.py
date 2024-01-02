#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""

from sys import argv
import requests


if __name__ == "__main__":
    URL = "http://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(URL, argv[1])).json()
    todos = requests.get("{}/todos?userId={}".format(URL, argv[1])).json()
    done = requests.get("{}/todos?userId={}{}".format(URL, argv[1],
                                                      "&completed=true"
                                                      )).json()
    EMPLOYEE_NAME = user.get("name")
    NUMBER_OF_DONE_TASKS = len(done)
    TOTAL_NUM_OF_TASKS = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in done:
        print("\t {}".format(task.get("title")))
