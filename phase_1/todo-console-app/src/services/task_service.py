"""
Task Service
Task: T007, T013, T019, T026, T032, T037
Spec: speckit.specify FR-1.1, FR-1.2, FR-1.4, FR-1.5, FR-1.6, FR-1.7
Plan: speckit.plan Component 3
"""

from datetime import datetime
from typing import List, Optional

# Handle both module and direct execution
try:
    # Try relative import first (for when run as module)
    from ..models.task import Task
    from ..storage.memory_store import MemoryStore
except (ImportError, ValueError):
    # Fall back to absolute import (for when run directly)
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from models.task import Task
    from storage.memory_store import MemoryStore


class TaskService:
    """
    Business logic layer that coordinates between UI and storage.
    """
    
    def __init__(self):
        """
        Initialize the task service with a memory store.
        """
        self._store = MemoryStore()

    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create and store a new task.
        
        Args:
            title: The task title (required)
            description: The task description (optional)
            
        Returns:
            The created task with assigned ID
        """
        # Create a new task with ID 0 (will be assigned by store)
        task = Task(0, title, description, False)
        task_id = self._store.add(task)
        
        # Update the task's ID and return it
        task.id = task_id
        return task

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all tasks
        """
        return self._store.get_all()

    def get_task(self, id: int) -> Optional[Task]:
        """
        Get a specific task by ID.
        
        Args:
            id: The ID of the task to retrieve
            
        Returns:
            The task if found, None otherwise
        """
        return self._store.get(id)

    def update_task(self, id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task's title and/or description.
        
        Args:
            id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            The updated task if found, None otherwise
        """
        task = self._store.get(id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            task.updated_at = datetime.now()
            return task
        return None

    def delete_task(self, id: int) -> bool:
        """
        Remove a task by ID.
        
        Args:
            id: The ID of the task to remove
            
        Returns:
            True if the task was found and deleted, False otherwise
        """
        return self._store.delete(id)

    def toggle_complete(self, id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.
        
        Args:
            id: The ID of the task to toggle
            
        Returns:
            The updated task if found, None otherwise
        """
        task = self._store.get(id)
        if task:
            task.completed = not task.completed
            task.updated_at = datetime.now()
            return task
        return None