---

description: "Task list template for feature implementation"
---

# Tasks: Todo Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13+ project with UV
- [X] T003 [P] Create pyproject.toml with project metadata
- [X] T004 [P] Create all necessary folders (src/, models/, services/, storage/, ui/)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Create Task model in src/models/task.py
- [X] T006 [P] Create MemoryStore in src/storage/memory_store.py
- [X] T007 [P] Create TaskService base structure in src/services/task_service.py
- [X] T008 [P] Create ConsoleUI base structure in src/ui/console.py
- [X] T009 Create main entry point in src/main.py
- [X] T010 Create __init__.py files in all package directories

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: User can create a new task in their todo list with a title and optional description

**Independent Test**: User can launch the application, select the "Add Task" option, enter a title and optional description, and see the task created with a unique ID.

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement Task class with all properties and validation in src/models/task.py
- [X] T012 [P] [US1] Implement MemoryStore.add(task) method in src/storage/memory_store.py
- [X] T013 [US1] Implement TaskService.create_task method in src/services/task_service.py
- [X] T014 [US1] Implement ConsoleUI.add_task_flow method in src/ui/console.py
- [X] T015 [US1] Implement ConsoleUI._get_input helper with validation in src/ui/console.py
- [X] T016 [US1] Connect add task flow to main menu in src/ui/console.py
- [X] T017 [US1] Add type hints and docstrings to all new methods

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P2)

**Goal**: User can see all their tasks in one place with ID, title, and completion status

**Independent Test**: User can view all tasks with their ID, title, and completion status in a clear format.

### Implementation for User Story 2

- [X] T018 [P] [US2] Implement MemoryStore.get_all() method in src/storage/memory_store.py
- [X] T019 [P] [US2] Implement TaskService.list_tasks method in src/services/task_service.py
- [X] T020 [US2] Implement ConsoleUI._display_tasks helper in src/ui/console.py
- [X] T021 [US2] Implement ConsoleUI.view_tasks_flow method in src/ui/console.py
- [X] T022 [US2] Connect view tasks flow to main menu in src/ui/console.py
- [X] T023 [US2] Handle empty list case with appropriate message in src/ui/console.py
- [X] T024 [US2] Add type hints and docstrings to all new methods

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: User can modify the title or description of an existing task

**Independent Test**: User can select a task by ID and update its title or description.

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement MemoryStore.update(id, updates) method in src/storage/memory_store.py
- [X] T026 [P] [US3] Implement TaskService.update_task method in src/services/task_service.py
- [X] T027 [US3] Implement ConsoleUI.update_task_flow method in src/ui/console.py
- [X] T028 [US3] Connect update task flow to main menu in src/ui/console.py
- [X] T029 [US3] Add validation for task existence in src/services/task_service.py
- [X] T030 [US3] Add type hints and docstrings to all new methods

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P4)

**Goal**: User can remove tasks they no longer need

**Independent Test**: User can select a task by ID and remove it from the system.

### Implementation for User Story 4

- [X] T031 [P] [US4] Implement MemoryStore.delete(id) method in src/storage/memory_store.py
- [X] T032 [P] [US4] Implement TaskService.delete_task method in src/services/task_service.py
- [X] T033 [US4] Implement ConsoleUI.delete_task_flow method in src/ui/console.py
- [X] T034 [US4] Connect delete task flow to main menu in src/ui/console.py
- [X] T035 [US4] Add validation for task existence in src/services/task_service.py
- [X] T036 [US4] Add type hints and docstrings to all new methods

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete (Priority: P5)

**Goal**: User can mark tasks as completed to track their progress

**Independent Test**: User can toggle the completion status of a task by ID.

### Implementation for User Story 5

- [X] T037 [P] [US5] Implement TaskService.toggle_complete method in src/services/task_service.py
- [X] T038 [US5] Implement ConsoleUI.complete_task_flow method in src/ui/console.py
- [X] T039 [US5] Connect complete task flow to main menu in src/ui/console.py
- [X] T040 [US5] Add validation for task existence in src/services/task_service.py
- [X] T041 [US5] Add type hints and docstrings to all new methods

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T042 [P] Update README.md with usage examples
- [X] T043 [P] Create CLAUDE.md with development instructions
- [X] T044 [P] Create .gitignore with appropriate entries
- [X] T045 [P] Create .spec-kit/config.yaml
- [X] T046 Code cleanup and refactoring
- [X] T047 Manual testing of all features
- [X] T048 [P] Error handling for edge cases (invalid inputs, non-existent IDs)
- [X] T049 [P] Add graceful exit functionality to main menu
- [X] T050 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task class with all properties and validation in src/models/task.py"
Task: "Implement MemoryStore.add(task) method in src/storage/memory_store.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence