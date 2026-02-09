# Implementation Plan: Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-29 | **Spec**: [specs/001-todo-console-app/spec.md](../001-todo-console-app/spec.md)
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a console-based todo application in Python with in-memory storage. The application will support the 5 basic features: Add Task, Delete Task, Update Task, View Task List, and Mark as Complete. The architecture follows a layered approach with clear separation of concerns between presentation (UI), business logic (services), and data (models/storage).

## Technical Context

**Language/Version**: Python 3.13+ (as required by constitution)
**Primary Dependencies**: Python standard library only (as required by constitution)
**Storage**: In-memory dictionary-based storage (as required by constitution)
**Testing**: Manual testing via console interface (as specified in requirements)
**Target Platform**: Cross-platform console application (Windows, macOS, Linux)
**Project Type**: Single console application
**Performance Goals**: < 100ms response time for all operations, < 1 second startup time (as specified in requirements)
**Constraints**: No external dependencies, in-memory storage only, console interface only (as required by constitution)
**Scale/Scope**: Single-user application, up to 1000 tasks with < 100MB memory usage (as specified in requirements)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-Driven Development: Following the Spec-Kit workflow as required
- ✅ Python 3.13+ Technology Constraint: Using Python 3.13+ as required
- ✅ Clean Code and Python Best Practices: Will implement type hints, docstrings, and follow PEP 8
- ✅ Test-First Approach: Will ensure code is testable with separation of concerns
- ✅ Console-Based Interface: Implementing CLI interface as required
- ✅ In-Memory Storage Design: Using Python data structures for storage as required
- ✅ Code Standards: Will implement type hints, docstrings, and follow all code standards from constitution

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
todo-console-app/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── speckit.constitution
│   ├── speckit.specify
│   ├── speckit.plan
│   └── speckit.tasks
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py       # Task data model
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Business logic
│   ├── storage/
│   │   ├── __init__.py
│   │   └── memory_store.py  # In-memory storage
│   └── ui/
│       ├── __init__.py
│       └── console.py    # CLI interface
├── tests/
│   └── __init__.py
├── CLAUDE.md
├── README.md
├── pyproject.toml
└── .gitignore
```

**Structure Decision**: Single console application with layered architecture following separation of concerns as required by constitution. The structure includes models for data representation, services for business logic, storage for data persistence, and UI for user interaction.

## Architecture Overview

The application follows a layered architecture pattern with clear separation of concerns:

```
┌─────────────────┐
│   UI Layer      │ ← Console interface handling user input/output
├─────────────────┤
│  Service Layer  │ ← Business logic and coordination
├─────────────────┤
│  Model Layer    │ ← Data structures and validation
├─────────────────┤
│  Storage Layer  │ ← In-memory data storage
└─────────────────┘
```

**Component Responsibilities:**
- **UI Layer**: Handles user interaction, displays menus, collects input, shows results
- **Service Layer**: Implements business rules, coordinates operations, validates inputs
- **Model Layer**: Defines data structures and provides data validation
- **Storage Layer**: Manages in-memory storage of tasks

**Data Flow:**
- User interactions flow from UI → Service → Storage → Service → UI
- All business logic is encapsulated in the service layer
- Data validation occurs at both UI and service layers

## Component Design

### Component 1: Task Model (`src/models/task.py`)
- **Purpose**: Define Task data structure
- **Responsibilities**:
  - Task class with properties (id, title, description, completed, timestamps)
  - Data validation methods
  - String representation for display
- **Key Methods**:
  - `__init__()`: Initialize task with validation
  - `to_dict()`: Convert to dictionary
  - `from_dict()`: Create from dictionary
  - `__str__()`: Display format

### Component 2: Memory Store (`src/storage/memory_store.py`)
- **Purpose**: Manage in-memory task storage
- **Responsibilities**:
  - Store tasks in dictionary for O(1) lookups
  - Generate unique IDs
  - Provide CRUD operations interface
- **Key Methods**:
  - `add(task)`: Store new task, return ID
  - `get(id)`: Retrieve task by ID
  - `get_all()`: Return all tasks
  - `update(id, updates)`: Modify task
  - `delete(id)`: Remove task
  - `_generate_id()`: Create unique ID

### Component 3: Task Service (`src/services/task_service.py`)
- **Purpose**: Business logic layer
- **Responsibilities**:
  - Coordinate between UI and storage
  - Validate inputs
  - Handle timestamps
  - Implement business rules
- **Key Methods**:
  - `create_task(title, description)`: Create and store new task
  - `list_tasks()`: Get all tasks
  - `get_task(id)`: Get specific task
  - `update_task(id, title, description)`: Update task
  - `delete_task(id)`: Remove task
  - `toggle_complete(id)`: Toggle completion status

### Component 4: Console UI (`src/ui/console.py`)
- **Purpose**: User interaction layer
- **Responsibilities**:
  - Display menu
  - Handle user input
  - Show task information
  - Display messages and errors
- **Key Methods**:
  - `run()`: Main application loop
  - `display_menu()`: Show menu options
  - `get_user_choice()`: Get menu selection
  - `add_task_flow()`: Handle add task interaction
  - `view_tasks_flow()`: Display task list
  - `update_task_flow()`: Handle update interaction
  - `delete_task_flow()`: Handle delete interaction
  - `complete_task_flow()`: Handle completion toggle
  - `_display_tasks(tasks)`: Format and show tasks
  - `_get_input(prompt, required, max_length)`: Validated input

### Component 5: Main (`src/main.py`)
- **Purpose**: Application entry point
- **Responsibilities**:
  - Initialize components
  - Handle top-level exceptions
  - Clean exit
- **Key Methods**:
  - `main()`: Setup and launch application

## Data Flow

### Flow 1: Add Task
```
User → Console.add_task_flow()
     → Get title input (validated)
     → Get description input (optional)
     → TaskService.create_task(title, description)
          → Create Task object
          → MemoryStore.add(task)
               → Generate ID
               → Store in dictionary
               → Return ID
          → Return created task
     → Display confirmation
```

### Flow 2: View Tasks
```
User → Console.view_tasks_flow()
     → TaskService.list_tasks()
          → MemoryStore.get_all()
               → Return list of all tasks
          → Return tasks
     → Console._display_tasks(tasks)
          → Format each task
          → Print to console
```

### Flow 3: Update Task
```
User → Console.update_task_flow()
     → Get task ID input
     → TaskService.get_task(id)  # Verify exists
     → Get new title (optional)
     → Get new description (optional)
     → TaskService.update_task(id, title, description)
          → MemoryStore.update(id, updates)
               → Update task in storage
               → Update timestamp
               → Return updated task
          → Return updated task
     → Display confirmation
```

## Error Handling Strategy
- Input validation at UI layer with clear error messages
- Business rule validation at service layer
- Not found errors return None, handled gracefully
- All user-facing errors show friendly messages
- Technical errors logged for debugging
- Graceful exit handling

## Data Structures

### Storage Structure:
```python
{
    1: Task(id=1, title="...", ...),
    2: Task(id=2, title="...", ...),
    ...
}
```
- Use dictionary for O(1) lookups
- Keys are integer IDs
- Values are Task objects

### ID Generation:
- Start at 1
- Increment counter for each new task
- Store counter in MemoryStore

## Menu Structure
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

## Implementation Sequence
1. Task Model (foundation)
2. Memory Store (storage layer)
3. Task Service (business logic)
4. Console UI (user interface)
5. Main entry point
6. Testing and refinement

## Testing Approach
- Manual testing via console
- Test each feature independently
- Test error cases (invalid IDs, empty inputs)
- Test edge cases (empty list, long text)

## Migration Readiness (for Phase II)
Design considerations for database migration:
- Task model structure matches future SQLModel schema
- Service layer abstraction allows storage swapping
- ID generation will be replaced by database auto-increment
- Timestamps ready for database timestamp fields

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |