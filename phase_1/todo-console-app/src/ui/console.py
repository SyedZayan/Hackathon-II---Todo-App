"""
Console UI
Task: T008, T014, T015, T016, T020, T021, T022, T027, T028, T033, T034, T038, T039
Spec: speckit.specify FR-2.1, FR-2.2, FR-2.3, FR-2.4, FR-3.1, FR-3.2, FR-3.3
Plan: speckit.plan Component 4
"""

from typing import Optional

# Handle both module and direct execution
try:
    # Try relative import first (for when run as module)
    from ..services.task_service import TaskService
except (ImportError, ValueError):
    # Fall back to absolute import (for when run directly)
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from services.task_service import TaskService


class ConsoleUI:
    """
    User interaction layer that handles console interface.
    """
    
    def __init__(self):
        """
        Initialize the console UI with a task service.
        """
        self._task_service = TaskService()
        self._running = True

    def run(self):
        """
        Main application loop.
        """
        print("=== Todo Application ===")
        while self._running:
            self.display_menu()
            choice = self.get_user_choice()
            self._handle_choice(choice)

    def display_menu(self):
        """
        Show menu options.
        """
        print("\n=== Todo Application ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print()

    def get_user_choice(self) -> int:
        """
        Get menu selection from user.
        
        Returns:
            The user's menu choice
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid number.")

    def add_task_flow(self):
        """
        Handle add task interaction.
        """
        print("\n--- Add New Task ---")
        title = self._get_input("Enter task title (1-200 characters): ", required=True, max_length=200)
        if title is None:
            return  # User cancelled
            
        description = self._get_input("Enter task description (optional, max 1000 characters): ", 
                                     required=False, max_length=1000)
        
        try:
            task = self._task_service.create_task(title, description)
            print(f"Task created successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error creating task: {e}")

    def view_tasks_flow(self):
        """
        Display task list.
        """
        print("\n--- Task List ---")
        tasks = self._task_service.list_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
            
        self._display_tasks(tasks)

    def update_task_flow(self):
        """
        Handle update task interaction.
        """
        print("\n--- Update Task ---")
        tasks = self._task_service.list_tasks()
        
        if not tasks:
            print("No tasks available to update.")
            return
            
        self._display_tasks(tasks)
        
        task_id = self._get_input_int("Enter task ID to update: ", required=True)
        if task_id is None:
            return  # User cancelled
            
        task = self._task_service.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
            
        new_title = self._get_input(f"Enter new title (current: {task.title}) [Press Enter to keep current]: ", 
                                   required=False, max_length=200)
        if new_title == "":  # User pressed Enter to keep current
            new_title = None
            
        new_description = self._get_input(f"Enter new description (current: {task.description}) [Press Enter to keep current]: ", 
                                        required=False, max_length=1000)
        if new_description == "":  # User pressed Enter to keep current
            new_description = None
            
        try:
            updated_task = self._task_service.update_task(task_id, new_title, new_description)
            if updated_task:
                print("Task updated successfully.")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error updating task: {e}")

    def delete_task_flow(self):
        """
        Handle delete task interaction.
        """
        print("\n--- Delete Task ---")
        tasks = self._task_service.list_tasks()
        
        if not tasks:
            print("No tasks available to delete.")
            return
            
        self._display_tasks(tasks)
        
        task_id = self._get_input_int("Enter task ID to delete: ", required=True)
        if task_id is None:
            return  # User cancelled
            
        task = self._task_service.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
            
        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ")
        if confirm.lower() == 'y':
            success = self._task_service.delete_task(task_id)
            if success:
                print("Task deleted successfully.")
            else:
                print("Failed to delete task.")
        else:
            print("Deletion cancelled.")

    def complete_task_flow(self):
        """
        Handle completion toggle interaction.
        """
        print("\n--- Mark Task Complete/Incomplete ---")
        tasks = self._task_service.list_tasks()
        
        if not tasks:
            print("No tasks available to mark.")
            return
            
        self._display_tasks(tasks)
        
        task_id = self._get_input_int("Enter task ID to toggle completion: ", required=True)
        if task_id is None:
            return  # User cancelled
            
        task = self._task_service.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
            
        updated_task = self._task_service.toggle_complete(task_id)
        if updated_task:
            status = "completed" if updated_task.completed else "incomplete"
            print(f"Task marked as {status}.")
        else:
            print("Failed to update task completion status.")

    def _display_tasks(self, tasks):
        """
        Format and show tasks.
        
        Args:
            tasks: List of tasks to display
        """
        print("\nID | Status | Title")
        print("-" * 50)
        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"{task.id:2d} |   {status}    | {task.title}")

    def _get_input(self, prompt: str, required: bool, max_length: Optional[int] = None):
        """
        Get validated input from user.

        Args:
            prompt: The prompt to display to the user
            required: Whether the input is required
            max_length: Maximum length for string inputs (None for no limit)

        Returns:
            The user's input, or None if cancelled
        """
        while True:
            try:
                user_input = input(prompt)

                if required and not user_input.strip():
                    print("This field is required. Please enter a value.")
                    continue

                if max_length is not None and len(user_input) > max_length:
                    print(f"Input too long. Maximum {max_length} characters allowed.")
                    continue

                return user_input
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None

    def _get_input_int(self, prompt: str, required: bool):
        """
        Get validated integer input from user.

        Args:
            prompt: The prompt to display to the user
            required: Whether the input is required

        Returns:
            The user's integer input, or None if cancelled
        """
        while True:
            try:
                user_input = input(prompt)

                if required and not user_input.strip():
                    print("This field is required. Please enter a value.")
                    continue
                elif not user_input.strip():
                    return None

                try:
                    return int(user_input)
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None

    def _handle_choice(self, choice: int):
        """
        Handle the user's menu choice.
        
        Args:
            choice: The user's menu choice
        """
        if choice == 1:
            self.add_task_flow()
        elif choice == 2:
            self.view_tasks_flow()
        elif choice == 3:
            self.update_task_flow()
        elif choice == 4:
            self.delete_task_flow()
        elif choice == 5:
            self.complete_task_flow()
        elif choice == 6:
            print("Goodbye!")
            self._running = False