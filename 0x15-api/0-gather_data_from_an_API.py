#!/usr/bin/python3
"""
This module fetches and displays an employee's TODO list progress
using a REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress of an employee."""
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url).json()
    employee_name = user_response.get("name")

    # Fetch TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url).json()

    # Process TODO list data
    total_tasks = len(todos_response)
    done_tasks = [task for task in todos_response if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
