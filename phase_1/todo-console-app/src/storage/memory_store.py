"""
Memory Store
Task: T006, T012, T018, T025, T031
Spec: speckit.specify FR-1.3, FR-1.4, FR-1.5, FR-1.6
Plan: speckit.plan Component 2
"""

from datetime import datetime
from typing import Dict, List, Optional

# Handle both module and direct execution
try:
    # Try relative import first (for when run as module)
    from ..models.task import Task
except (ImportError, ValueError):
    # Fall back to absolute import (for when run directly)
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from models.task import Task


class MemoryStore:
    """
    Manage in-memory task storage using a dictionary for O(1) lookups.
    """

    def __init__(self):
        """
        Initialize the memory store with an empty task dictionary and ID counter.
        """
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> int:
        """
        Store a new task and return its assigned ID.

        Args:
            task: The task to store

        Returns:
            The ID assigned to the task
        """
        task.id = self._generate_id()
        self._tasks[task.id] = task
        return task.id

    def get(self, id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(id)

    def get_all(self) -> List[Task]:
        """
        Return all tasks.

        Returns:
            List of all tasks in the store
        """
        return list(self._tasks.values())

    def update(self, id: int, updates: Dict) -> Optional[Task]:
        """
        Update a task with the provided fields.

        Args:
            id: The ID of the task to update
            updates: Dictionary of fields to update

        Returns:
            The updated task if found, None otherwise
        """
        task = self._tasks.get(id)
        if task:
            for key, value in updates.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            task.updated_at = datetime.now()
            return task
        return None

    def delete(self, id: int) -> bool:
        """
        Remove a task by its ID.

        Args:
            id: The ID of the task to remove

        Returns:
            True if the task was found and deleted, False otherwise
        """
        if id in self._tasks:
            del self._tasks[id]
            return True
        return False

    def _generate_id(self) -> int:
        """
        Generate a unique ID for a new task.

        Returns:
            A unique integer ID
        """
        new_id = self._next_id
        self._next_id += 1
        return new_id