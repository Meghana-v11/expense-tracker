# Expense Tracker — v3

A full rewrite of my expense tracker using Object-Oriented Programming, file handling, and
exception handling — the biggest step up yet from v1 (plain scripting) and v2 (functions).

## Features
Same core functionality as v1/v2 — add, view, delete, view-deleted, edit, search, monthly
summary, exit — now backed by two classes, persistent JSON storage, and proper error handling
throughout.

## What's new compared to v2

**Object-Oriented Design**
- `Expense` class: represents a single expense as an object (id, amount, category, description,
  date) instead of a plain dictionary
- `ExpenseTracker` class: manages the collection of expenses (`self.expenses`, a dictionary keyed
  by expense id for fast lookups) and exposes all operations as methods
- Replaced the `global` variable trick from v2 (`last_deleted`) with a proper instance attribute
  (`self.last_deleted`) — a cleaner, more scalable way to share state between methods
- Used `setattr()` to dynamically update an object's attribute by field name during editing,
  instead of dictionary-style key assignment

**File Handling (data persistence)**
- Expenses are saved to a JSON file (`expenses.json`) after every add, delete, or edit — no more
  losing all data when the program closes
- On startup, existing data is automatically loaded back in
- Added `to_dict()` on `Expense` to convert objects into plain dictionaries for JSON serialization,
  and used `Expense(**data)` to reconstruct objects from loaded JSON

**Exception Handling**
- Wrapped all numeric input (`int(input(...))`) in `try`/`except ValueError` so invalid input
  no longer crashes the program
- Handled `FileNotFoundError` for first-time runs (no save file yet) and `json.JSONDecodeError`
  for a missing/corrupted/empty save file

## What I learned
- Designing a program around classes and objects instead of standalone functions and dictionaries
- The difference between dictionary access (`dict[key]`) and object attribute access
  (`obj.attribute`), and why `setattr()` is needed to set an attribute dynamically by name
- Serializing custom objects to JSON by converting them to plain dictionaries first, and
  reconstructing them on load
- Writing exception handling that actually stops execution on failure (`return`/`continue`),
  not just catching the error and letting the code crash one line later
- Debugging real runtime errors (tracebacks) from file I/O and JSON parsing, not just syntax errors

## How to run
```bash
python expenseversion3.py
```
Data is saved automatically to `expenses.json` in the same folder, and reloaded automatically the
next time the program runs.

## Known limitations
- Category/description search is case-sensitive and requires an exact match
- No support for editing/deleting multiple expenses at once
- Single flat JSON file — not suitable for large datasets (would move to a proper database next)

## Next steps
- Add case-insensitive and partial-match search
- Move storage from JSON to SQLite for more robust data handling
- Add unit tests
- Possibly wrap in a simple CLI framework or basic GUI
