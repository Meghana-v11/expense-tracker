# Expense Tracker — v2

A refactored version of my v1 expense tracker, rebuilt using functions to practice writing modular,
reusable Python code instead of one long procedural script.

## Features
Same features as v1 — add, view, delete, view-deleted, edit, search, monthly summary, exit —
now organized into functions instead of inline logic.

## What's new compared to v1
- Each menu option is now its own function (`add_expense`, `view_expense`, `delete_expense`, etc.)
  instead of inline code inside the main loop
- Introduced a shared `print_expense()` helper function, reused across `view_expense`,
  `view_deleted_expense`, and `search_expense` to avoid repeating the same print logic
  (DRY principle — Don't Repeat Yourself)
- `search_expense()` uses one generic function with a `field` parameter instead of writing
  three near-identical search blocks
- Used a `global` variable (`last_deleted`) to let `delete_expense()` and `view_deleted_expense()`
  share data across function calls — and learned why this is a useful but limited pattern
  (to be replaced with a class attribute in v3)

## What I learned
- Writing and calling functions with parameters and return values
- Reducing code duplication by extracting shared logic into helper functions
- Scope in Python: why variables inside a function disappear afterward, and how `global`
  works (and its limitations, which motivated wanting to learn OOP next)
- Using a dictionary to map user choices to field names, instead of repeating if/elif blocks

## How to run
```bash
python expenseversion2.py
```
Follow the on-screen menu (1-8) to interact with the tracker. Data is stored in memory only
and is lost when the program exits.

## Known limitations (by design, for this version)
- No error handling for invalid input types
- Data does not persist between runs
- Search is case-sensitive and requires exact matches

## Next steps
- v3: Rewrite using OOP (a class-based `ExpenseTracker`), add file handling to save/load data,
  and add exception handling for invalid input
