# Todo Console App

A simple console-based todo application with in-memory storage, built in Python.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Simple console menu interface

## Requirements

- Python 3.13+
- UV package manager

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies with UV:
   ```bash
   uv sync
   ```

## Usage

Run the application:
```bash
uv run python src/main.py
```

Follow the on-screen menu prompts to manage your tasks.

## Project Structure

```
todo-console-app/
├── src/
│   ├── main.py           # Entry point
│   ├── models/
│   │   └── task.py       # Task data model
│   ├── services/
│   │   └── task_service.py  # Business logic
│   ├── storage/
│   │   └── memory_store.py  # In-memory storage
│   └── ui/
│       └── console.py    # CLI interface
```

## Architecture

The application follows a layered architecture:
- **UI Layer**: Console interface handling user input/output
- **Service Layer**: Business logic and coordination
- **Model Layer**: Data structures and validation
- **Storage Layer**: In-memory data storage