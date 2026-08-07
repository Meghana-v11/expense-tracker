print("---EXPENSE TRACKER---")
expense_tracker = []
print("1. Add an expense")
print("2. View an expense")
print("3. Delete an expense")
print("4. View deleted expense")
print("5. Edit an expense")
print("6. Search for an expense")
print("7. Monthly spending summary")
print("8. Exit")
def add_expense():
    expense_dict = {
        "id" : int(input("Enter Id:")),
        "amount" : int(input("Enter amount:")),
        "category" : input("Enter category:"),
        "description" : input("Enter description:"),
        "date" : input("Enter date:")
    }
    expense_tracker.append(expense_dict)
    print("Your expense is added.")
def print_expense(expense):
    print("------------------------")
    for key, value in expense.items():
            print(f"{key}: {value}")
    print("------------------------")
def view_expense():
    for expense in expense_tracker:
        print_expense(expense)
last_deleted = None
def delete_expense(del_id):
    global last_deleted
    last_deleted = next((exp for exp in expense_tracker if exp.get("id") == del_id), None)
    new_list = [exp for exp in expense_tracker if exp["id"] != del_id]
    print("Expense deleted successfully.")
    return new_list
def view_deleted_expense():
    if last_deleted:
        print("Deleted dictionary")
        print_expense(last_deleted)
    else:
        print("No expense has been deleted yet.")
def edit_expense(edit_id):
    for expense in expense_tracker:
        if expense["id"] == edit_id:
            print("""what do you want to edit?
                    1. Amount
                    2. Category
                    3. Description
                    4. Date""")
            edit_choice = int(input("Enter your choice:"))
            fields = {
                1: "amount",
                2: "category",
                3: "description",
                4: "date"
            }
            if edit_choice in fields:
                field = fields[edit_choice]
                if field == "amount":
                    expense[field] = int(input(f"Enter new {field}:"))
                else:
                    expense[field] = input(f"Enter new {field}:")
            else:
                print("Invalid choice.")
def search_expense():
    print("searching for an expense")
    print("""What do you want to search by?
            1. id
            2. Category
            3. Description""")
    search_choice = int(input("Enter your choice:"))
    if search_choice == 1:
        search_value = int(input("Enter id:"))
        field = "id"
    elif search_choice == 2:
        search_value = input("Enter category:")
        field = "category"
    elif search_choice == 3:
        search_value = input("Enter description:")
        field = "description"
    else:
        print("Invalid choice.")
        return
    found = False 
    for expense in expense_tracker:
        if field == "id" and expense["id"] == search_value:
            print_expense(expense)
            found = True
        elif field == "category" and expense["category"] == search_value:
            print_expense(expense)
            found = True
        elif field == "description" and expense["description"] == search_value:
            print_expense(expense)
            found = True
    if not found:
        print("NO matching expense found.")
def monthly_expense():
    month = input("Enter month (MM-YYYY):")
    total = 0
    for expense in expense_tracker:
        if month in expense["date"]:
            total += expense["amount"]
    print("Monthly Spending Summary")
    print(f"Month: {month}")
    if total == 0:
        print("No expenses found for this month")
    else:
        print(f"Total spending: {total}")
while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        del_id = int(input("Enter id to delete:"))
        expense_tracker = delete_expense(del_id)
    elif choice == 4:
        view_deleted_expense()
    elif choice == 5:
        edit_id = int(input("Enter id to edit:"))
        edit_expense(edit_id)
    elif choice == 6:
        search_expense()
    elif choice == 7:
        monthly_expense()
    elif choice == 8:
        break
