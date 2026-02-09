<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All sections
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending - needs constitution check alignment
  - .specify/templates/spec-template.md ⚠ pending - needs requirement validation
  - .specify/templates/tasks-template.md ⚠ pending - needs task categorization update
  - .qwen/commands/*.toml ⚠ pending - needs workflow validation
  - README.md ⚠ pending - needs project setup instructions
- Follow-up TODOs: None
-->

# Todo Hackathon Phase I Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All features must be specified before implementation using the Spec-Kit workflow: Specify → Plan → Tasks → Implement. No feature implementation without corresponding spec. Each task must reference specification sections.

### II. Python 3.13+ Technology Constraint
Use Python 3.13+ exclusively with UV package manager. Standard library preferred with minimal external dependencies. This ensures consistency and compatibility across development environments.

### III. Clean Code and Python Best Practices
Follow PEP 8 guidelines, require type hints for all functions, and implement Google-style docstrings for all classes and functions. Each function should have a single responsibility with maximum 30 lines length.

### IV. Test-First Approach
Code must be testable with comprehensive unit tests. All business logic must be separated from input/output operations to ensure testability. Input validation required for all user inputs.

### V. Console-Based Interface
Implement a simple, intuitive CLI menu system using input/print for the console-based interface. No print statements in business logic - return values instead for proper separation of concerns.

### VI. In-Memory Storage Design
Use Python data structures (list/dict) for in-memory storage in Phase I. Design data structures with future database migration in mind for Phase II, ensuring clean separation between business logic and data storage layers.

## Technology Constraints

- Python 3.13+ only
- UV for package management
- Standard library preferred (minimal external dependencies)
- In-memory storage (no database in Phase I)
- Console-based interface using input/print
- No persistence between runs (acceptable for Phase I)

## Code Standards

- Type hints required for all functions
- Docstrings for all classes and functions (Google style)
- Maximum function length: 30 lines
- Meaningful variable names (no single letters except for loop indices)
- Error handling with try-except blocks where appropriate
- No print statements in business logic (return values instead)
- Graceful error messages for users

## Development Workflow

- Must use Spec-Kit workflow: Specify → Plan → Tasks → Implement
- Each task must reference specification sections
- No feature implementation without corresponding spec
- Documentation must be updated with code changes
- All implementation must be done via Claude Code (no manual coding)

## Project Structure

- Follow standard Python project structure
- Separation of concerns (models, services, UI)
- Configuration in separate file if needed
- README.md with clear setup instructions
- Focus on core CRUD operations

## Governance

This constitution governs all development activities for Phase I of the Todo Hackathon project. All code changes must comply with these principles. Amendments require documentation and approval. All PRs/reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2025-12-29
