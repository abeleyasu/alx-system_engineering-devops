#!/usr/bin/python3
"""
This module fetches an employee's TODO list progress using a REST API
and exports the data to a JSON file.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and export the TODO list progress of an employee."""
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url).json()
    username = user_response.get("username")

    # Fetch TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url).json()

    # Process TODO list data
    todo_list = []
    for task in todos_response:
        todo_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Export data to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as file:
        json.dump({str(employee_id): todo_list}, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
