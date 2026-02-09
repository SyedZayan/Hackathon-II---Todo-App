#!/usr/bin/env python3
"""
Manual testing script for the Todo Console App
Task: T047
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'todo-console-app', 'src'))

from models.task import Task
from storage.memory_store import MemoryStore
from services.task_service import TaskService
from ui.console import ConsoleUI


def test_task_creation():
    """Test creating a task"""
    print("Testing task creation...")
    service = TaskService()
    
    # Create a task
    task = service.create_task("Test task", "This is a test task")
    assert task.title == "Test task"
    assert task.description == "This is a test task"
    assert task.completed == False
    print("✓ Task creation works")


def test_task_retrieval():
    """Test retrieving tasks"""
    print("Testing task retrieval...")
    service = TaskService()
    
    # Create a task
    task = service.create_task("Retrieve test", "Test retrieval")
    
    # Get the task back
    retrieved = service.get_task(task.id)
    assert retrieved is not None
    assert retrieved.id == task.id
    assert retrieved.title == "Retrieve test"
    print("✓ Task retrieval works")


def test_task_list():
    """Test listing tasks"""
    print("Testing task listing...")
    service = TaskService()
    
    # Create a few tasks
    service.create_task("List test 1", "First test")
    service.create_task("List test 2", "Second test")
    
    # Get all tasks
    tasks = service.list_tasks()
    assert len(tasks) >= 2
    print(f"✓ Task listing works, found {len(tasks)} tasks")


def test_task_update():
    """Test updating a task"""
    print("Testing task update...")
    service = TaskService()
    
    # Create a task
    task = service.create_task("Update test", "Original description")
    
    # Update the task
    updated = service.update_task(task.id, "Updated title", "Updated description")
    assert updated is not None
    assert updated.title == "Updated title"
    assert updated.description == "Updated description"
    print("✓ Task update works")


def test_task_deletion():
    """Test deleting a task"""
    print("Testing task deletion...")
    service = TaskService()
    
    # Create a task
    task = service.create_task("Delete test", "To be deleted")
    
    # Delete the task
    success = service.delete_task(task.id)
    assert success == True
    
    # Verify it's gone
    retrieved = service.get_task(task.id)
    assert retrieved is None
    print("✓ Task deletion works")


def test_task_completion():
    """Test toggling task completion"""
    print("Testing task completion toggle...")
    service = TaskService()
    
    # Create a task
    task = service.create_task("Completion test", "Toggle completion")
    
    # Verify initial state
    assert task.completed == False
    
    # Toggle completion
    updated = service.toggle_complete(task.id)
    assert updated is not None
    assert updated.completed == True
    
    # Toggle again
    updated2 = service.toggle_complete(task.id)
    assert updated2 is not None
    assert updated2.completed == False
    print("✓ Task completion toggle works")


def run_all_tests():
    """Run all manual tests"""
    print("Starting manual tests for Todo Console App...\n")
    
    test_task_creation()
    test_task_retrieval()
    test_task_list()
    test_task_update()
    test_task_deletion()
    test_task_completion()
    
    print("\n✓ All manual tests passed!")


if __name__ == "__main__":
    run_all_tests()