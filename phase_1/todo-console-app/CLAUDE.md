# Todo Console App - Development Guide

This document provides guidance for developing and extending the Todo Console App.

## Project Overview

The Todo Console App is a simple console-based todo application with in-memory storage. It follows a layered architecture with clear separation of concerns between presentation (UI), business logic (services), and data (models/storage).

## Architecture Layers

### UI Layer (`src/ui/`)
- Handles user interaction and console interface
- Contains menu systems and input validation
- Should not contain business logic

### Service Layer (`src/services/`)
- Contains business logic and coordination
- Validates inputs and manages data flow
- Orchestrates between UI and storage layers

### Model Layer (`src/models/`)
- Defines data structures and validation
- Contains entity definitions like Task
- Provides data transformation methods

### Storage Layer (`src/storage/`)
- Manages data persistence (in-memory for Phase I)
- Provides CRUD operations for entities
- Handles ID generation and storage management

## Development Guidelines

### Code Standards
- All functions must have type hints
- All classes and functions must have Google-style docstrings
- Maximum function length is 30 lines
- Use meaningful variable names
- Handle errors gracefully with appropriate messages

### Adding New Features
1. Update the specification if needed
2. Plan the implementation considering all layers
3. Implement in the appropriate layer
4. Ensure proper separation of concerns
5. Test the functionality manually

### Testing
- Test each feature manually through the console interface
- Verify error cases and edge cases
- Ensure all acceptance criteria are met

## Migration to Phase II

The current architecture is designed for easy migration to a database-backed system:
- Entity structures match future SQL schema
- Service layer abstraction allows storage swapping
- ID generation will be replaced by database auto-increment
- Timestamps are ready for database fields