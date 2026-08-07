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
while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Adding an expense")
        new_expense = {
            "id": int(input("Enter expense id:")),
            "amount": int(input("Enter amount:₹")),
            "category": input("Enter category:"),
            "description": input("Enter description:"),
            "date": input("Enter date:"),
        }
        expense_tracker.append(new_expense)
        print("Your expense is added")
    elif choice == 2:
        if expense_tracker != []:
            for expense in expense_tracker:
                print("------------------------")
                for key, value in expense.items():
                    print(f"{key}: {value}")
                print("------------------------")
        else:
            print("No expense is added yet")
    elif choice == 3:
        del_id = int(input("Enter the id of the expense to delete:"))
        deleted_dict = next((exp for exp in expense_tracker if exp.get("id")== del_id), None)
        expense_tracker = [exp for exp in expense_tracker if exp["id"] != del_id]
        print("Expense deleted successfully.")
    elif choice == 4:
        if 'deleted_dict' in locals() and deleted_dict is not None:
            print("Deleted dictionary")
            print("------------------------")
            for key, value in deleted_dict.items():
                print(f"{key}:{value}")
            print("------------------------")
        else:
            print("No expense has been deleted yet.")
    elif choice == 5:
        edit_id = int(input("Enter the id to edit:"))
        for exx in expense_tracker:
            if exx["id"] == edit_id:
                print("""what do you want to edit?
                1. Amount
                2. Category
                3. Description
                4. Date""")
                edit_choice = int(input("Choose the option you want to edit:"))
                if edit_choice == 1:
                    exx["amount"] = int(input("Enter new amount:"))
                    print("New amount is added")
                elif edit_choice == 2:
                    exx["category"] = input("Enter new category:")
                    print("New category is added")
                elif edit_choice == 3:
                    exx["description"] = input("Enter new description:")
                    print("New description is added")
                elif edit_choice == 4:
                    exx["date"] = input("Enter new date:")
                    print("New date is added")
                else:
                    print("Error, enter correct choice")
    elif choice == 6:
        print("""What do you want to search by?
              1. id
              2. Category
              3. Description""")
        search_choice = int(input("Enter your choice:"))
        if search_choice == 1:
            search_id = int(input("Enter id:"))
            found = False
            for expense in expense_tracker:
                if expense["id"] == search_id:
                    print("------------------------")
                    for key, value in expense.items():
                        print(f"{key}: {value}")
                    print("------------------------")
                    found = True
            if not found:
                print("No match found")
        if search_choice == 2:
            search_category = input("Enter category:")
            found = False
            for expense in expense_tracker:
                if expense["category"] == search_category:
                    print("------------------------")
                    for key, value in expense.items():
                        print(f"{key}: {value}")
                    print("------------------------")
                    found = True
            if not found:
                print("No match found")
        if search_choice == 3:
            search_description = input("Enter description:")
            found = False
            for expense in expense_tracker:
                if expense["description"] == search_description:
                    print("------------------------")
                    for key, value in expense.items():
                        print(f"{key}: {value}")
                    print("------------------------")
                    found = True
            if not found:
                print("No match found")
    elif choice == 7:
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
    elif choice == 8:
        break 