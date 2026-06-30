import csv
from datetime import datetime

expenses = []

def add_expense():
    today = datetime.now().strftime("%Y-%m-%d")
    category = input("Category: ")
    amount = input("Amount: ")

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, category, amount])


def view_expenses():
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for expense in reader:
            print(f"{expense['today']} {expense['category']}: {expense['amount']}")

def total_expenses():
    total = 0
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row['amount'])
        print(f"Total: {total}")

def search_expense():
    search = input("Search Category: ").lower()
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if row['category'].lower() == search:
                print(f"{row['today']} {row['category']}: {row['amount']}")
                found = True
                break
        if not found:
            print("Category not found!")
                
def delete_expense():
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for i, row in enumerate(rows):
            print(f"{i + 1}. {row['category']}")
    delete = int(input("Delete expense number: "))
    del rows[delete - 1]

    with open("expenses.csv", 'w', newline="") as f:
        fieldnames = ["today", "category", "amount"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)  

while True:
    print("""
    1. Add expense
    2. View expenses
    3. Total
    4. Search
    5. Delete
    6. Exit
    """)

    choice = input("> ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        break