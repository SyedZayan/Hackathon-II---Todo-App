#!/usr/bin/env python3
"""
Simple test to verify the Todo Console App functionality
Task: T047
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the main module and run
from src.main import main

if __name__ == "__main__":
    print("Starting the Todo Console App for manual testing...")
    print("Please test the following functionality manually:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update an existing task")
    print("4. Delete a task")
    print("5. Mark a task as complete/incomplete")
    print("6. Exit the application")
    print("\nRunning the application now...")
    main()