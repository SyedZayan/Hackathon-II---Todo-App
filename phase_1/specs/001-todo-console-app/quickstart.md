# Quickstart Guide: Todo Console App

**Feature**: Todo Console App
**Date**: 2025-12-29
**Status**: Complete

## Getting Started

This guide will help you set up and run the Todo Console App for the first time.

### Prerequisites

- Python 3.13+ installed on your system
- UV package manager (for dependency management)

### Setup Instructions

1. **Clone or create the project structure:**
   ```
   todo-console-app/
   ├── src/
   │   ├── __init__.py
   │   ├── main.py
   │   ├── models/
   │   │   ├── __init__.py
   │   │   └── task.py
   │   ├── services/
   │   │   ├── __init__.py
   │   │   └── task_service.py
   │   ├── storage/
   │   │   ├── __init__.py
   │   │   └── memory_store.py
   │   └── ui/
   │       ├── __init__.py
   │       └── console.py
   ├── pyproject.toml
   └── README.md
   ```

2. **Install dependencies (if any):**
   Since this project uses only the Python standard library, no additional dependencies need to be installed.

3. **Run the application:**
   ```bash
   cd todo-console-app
   python src/main.py
   ```

### Running the Application

Once you run the application, you'll see the main menu:

```
=== Todo Application ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

### Basic Usage

1. **Add a Task:**
   - Select option 1
   - Enter a title (1-200 characters)
   - Optionally enter a description (up to 1000 characters)
   - The system will assign a unique ID and confirm creation

2. **View Tasks:**
   - Select option 2
   - All tasks will be displayed with ID, title, and completion status

3. **Update a Task:**
   - Select option 3
   - Enter the task ID you want to update
   - Enter new title or description (or leave blank to keep current values)

4. **Delete a Task:**
   - Select option 4
   - Enter the task ID you want to delete
   - Confirm the deletion

5. **Mark Task Complete/Incomplete:**
   - Select option 5
   - Enter the task ID
   - The completion status will toggle

6. **Exit:**
   - Select option 6 to exit the application

### Troubleshooting

- **Application won't start**: Ensure you're using Python 3.13+ and running from the project root directory
- **Invalid input errors**: Check that titles are 1-200 characters and descriptions are under 1000 characters
- **Task not found errors**: Verify the task ID exists in the current session

### Development Notes

- The application stores all data in memory only - tasks will be lost when the application exits
- All business logic is separated from UI concerns
- The code follows PEP 8 standards with type hints and Google-style docstrings
- The architecture is designed for easy migration to a database in Phase II