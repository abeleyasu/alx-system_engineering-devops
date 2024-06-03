#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""

import json
import requests
from sys import argv


def export_to_json():
    """
    Exports data to JSON format.
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    all_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        tasks = []
        for todo in todos:
            if todo.get('userId') == user_id:
                task_data = {
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                }
                tasks.append(task_data)

        all_data[user_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file)


if __name__ == '__main__':
    export_to_json()
