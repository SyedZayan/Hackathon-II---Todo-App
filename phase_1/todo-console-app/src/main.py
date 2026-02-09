"""
Main Entry Point
Task: T009
Spec: speckit.specify Overall
Plan: speckit.plan Component 5
"""

import sys
import os

# Add the src directory to the path to allow imports when running directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Try relative import first (for when run as module)
    from .ui.console import ConsoleUI
except ImportError:
    # Fall back to absolute import (for when run directly)
    from ui.console import ConsoleUI


def main():
    """
    Setup and launch the application.
    """
    try:
        ui = ConsoleUI()
        ui.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Goodbye!")


if __name__ == "__main__":
    main()