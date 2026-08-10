import json
class Expense:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }
    def __str__(self):
        return f"ID: {self.expense_id} | Amount: {self.amount} | Category: {self.category} | Description: {self.description} | Date: {self.date}"
class ExpenseTracker:        
    def __init__(self):
        self.expenses = {}
        self.last_deleted = None
    def add_expense(self):
        while True:
            try:
                expense_id = int(input("Enter Id:"))
                break
            except ValueError:
                print("Enter correct value.")
        while True:
            try:
                amount = int(input("Enter amount:"))
                break
            except ValueError:
                print("Enter correct value")
        category = input("Enter category:")        
        description = input("Enter description:")
        date = input("Enter date:")
        new_expense = Expense(expense_id, amount, category, description, date) 
        self.expenses[expense_id] = new_expense
        print("Your expense is added")
        self.save_to_file("expenses.json")
    def save_to_file(self, filename):
        expense_list = []
        for expense in self.expenses.values():
            expense_list.append(expense.to_dict())
        with open(filename, "w") as f:
            json.dump(expense_list, f)
        print("Saved!")
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                expense_list = json.load(f)
            for data in expense_list:
                self.expenses[data["expense_id"]] = Expense(**data)
            print("Loaded!")
        except FileNotFoundError:
            print("No saved file yet, starting fresh.")
        except json.JSONDecodeError:
            print("Saved file is empty or corrupted, starting fresh.")
    def view_expense(self):
        for expense in self.expenses.values():
            print(expense)
    def delete_expense(self, del_id):
        self.last_deleted = self.expenses.pop(del_id, None)
        if self.last_deleted:
            print("Expense deleted successfully.")
        else:
            print("No expense with that id.")
        self.save_to_file("expenses.json")
    def view_deleted_expense(self):
        if self.last_deleted:
            print("Deleted expense:")
            print(self.last_deleted)
        else:
            print("No expense has been deleted yet.")
    def edit_expense(self, edit_id):
        for expense in self.expenses.values():
            if expense.expense_id == edit_id:
                print("""what do you want to edit?
                        1. Amount
                        2. Category
                        3. Description
                        4. Date""")
                try:
                    edit_choice = int(input("Enter your choice:"))
                except ValueError:
                    print("Enter correct value.")
                    return 
                fields = {
                    1: "amount",
                    2: "category",
                    3: "description",
                    4: "date"
                    }
                if edit_choice in fields:
                    field = fields[edit_choice]
                    if field == "amount":
                        try:
                            setattr(expense, field, int(input(f"Enter new {field}:")))
                        except ValueError:
                            print("Enter correct value")
                            return
                    else:
                        setattr(expense, field, input(f"Enter new {field}:"))
                    self.save_to_file("expenses.json")
                else:
                    print("Invalid choice.")
    def search_expense(self):
        print("searching for an expense")
        print("""What do you want to search by?
                1. id
                2. Category
                3. Description""")
        try:
            search_choice = int(input("Enter your choice:"))
        except ValueError:
            print("Enter correct value")
            return
        else:
            if search_choice == 1:
                try:
                    search_value = int(input("Enter id:"))
                except ValueError:
                    print("Enter correct value")
                    return
                else:
                    field = "expense_id"
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
        for expense in self.expenses.values():
            if field == "expense_id" and expense.expense_id == search_value:
                print(expense)
                found = True
            elif field == "category" and expense.category == search_value:
                print(expense)
                found = True
            elif field == "description" and expense.description == search_value:
                print(expense)
                found = True
        if not found:
            print("NO matching expense found.")
    def monthly_expense(self):
        month = input("Enter month (MM-YYYY):")
        total = 0
        for expense in self.expenses.values():
            if month in expense.date:
                total += expense.amount
        print("Monthly Spending Summary")
        print(f"Month: {month}")
        if total == 0:
            print("No expenses found for this month")
        else:
            print(f"Total spending: {total}")
tracker = ExpenseTracker()
tracker.load_from_file("expenses.json")
while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. View deleted expense")
    print("5. Edit expense")
    print("6. Search expense")
    print("7. Monthly summary")
    print("8. Exit")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Enter correct value.")
    else:
        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.view_expense()
        elif choice == 3:
            try:
                del_id = int(input("Enter id:"))
            except ValueError:
                print("Enter correct value")
            else:
                tracker.delete_expense(del_id)
        elif choice == 4:
            tracker.view_deleted_expense()
        elif choice == 5:
            try:
                edit_id = int(input("Enter id:"))
            except ValueError:
                print("Enter correct value")
            else:
                tracker.edit_expense(edit_id)
        elif choice == 6:
            tracker.search_expense()
        elif choice == 7:
            tracker.monthly_expense()
        elif choice == 8:
            tracker.save_to_file("expenses.json")
            break
    
        
                
        

 
        