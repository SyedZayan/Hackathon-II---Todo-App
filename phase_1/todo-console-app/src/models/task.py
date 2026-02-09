"""
Task Model
Task: T005, T011
Spec: speckit.specify §5 Data Model, FR-1.1, FR-1.2
Plan: speckit.plan Component 1
"""

from datetime import datetime
from typing import Optional


class Task:
    """
    Represents a single todo item with properties: id, title, description, 
    completion status, creation timestamp, and update timestamp.
    """
    
    def __init__(self, id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance with validation.
        
        Args:
            id: Unique identifier for the task
            title: The task title/description (1-200 characters)
            description: Additional details about the task (optional, max 1000 characters)
            completed: Completion status of the task (default: False)
        
        Raises:
            ValueError: If title is not between 1 and 200 characters,
                       or description exceeds 1000 characters
        """
        if not title or len(title) < 1 or len(title) > 200:
            raise ValueError("Title must be between 1 and 200 characters")
        if description and len(description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        self.id = id
        self.title = title
        self.description = description or ""
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Convert task to dictionary representation.
        
        Returns:
            Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """
        Create task from dictionary representation.
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            Task instance created from the dictionary data
        """
        task = cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description"),
            completed=data.get("completed", False)
        )
        # Restore timestamps if present
        if "created_at" in data:
            task.created_at = datetime.fromisoformat(data["created_at"])
        if "updated_at" in data:
            task.updated_at = datetime.fromisoformat(data["updated_at"])
        return task

    def __str__(self) -> str:
        """
        String representation for display.
        
        Returns:
            Formatted string representation of the task
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"