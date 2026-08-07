# Expense Tracker — v1

A command-line expense tracker built in Python as a beginner project to practice core programming
fundamentals: control flow, dictionaries, lists, and list comprehensions.

## Features
- Add an expense (id, amount, category, description, date)
- View all expenses
- Delete an expense by id
- View the most recently deleted expense
- Edit an existing expense (amount, category, description, or date)
- Search expenses by id, category, or description
- Monthly spending summary (filter by MM-YYYY)
- Exit the program

## What I learned
- Storing structured data using a list of dictionaries
- Using list comprehensions to filter data (e.g. deleting an expense)
- Using `next()` with a generator expression to find a single matching item
- Basic input validation and control flow with `while`/`if`/`elif`
- Debugging logic errors (e.g. incorrect variable references, crashes from missing data)

## How to run
```bash
python expensetracker.py
```
Follow the on-screen menu (1-8) to interact with the tracker. Note: all data is stored in memory
and is lost when the program exits — persistent storage (file/database) is planned for a future version.

## Known limitations (by design, for this version)
- No error handling for invalid input types (e.g. entering text where a number is expected)
- Category/description search is case-sensitive and requires an exact match
- Data does not persist between runs

## Next steps
- v2: Refactor into functions
- v3: Rewrite using OOP, add file handling for persistence, add exception handling
