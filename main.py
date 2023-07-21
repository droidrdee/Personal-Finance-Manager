# Personal Finance Manager

def add_expense():
    pass


def add_income():
    date = input('Enter date of income (DD-MM-YYYY) : ')
    source = input('Enter source of Income : ')
    amount = input('Enter amount of Income : ')

    income_entry = {
        "date": date,
        "source": source,
        "amount": amount
    }

    return income_entry


def check_balance(entry):
    print("Your current balance is : ",entry["amount"])


def categorize_expense():
    pass


def view_by_category():
    pass


def view_history():
    pass


def print_income(entries):
    for i in entries:
        print(i, " : ", entries[i])


# ---------------------------------------------------------------------


print("Welcome to your 'Personal Finance Manager'")

con = None

while con != 'n' or 'N':

    print("What do you want to do -")
    print("1. Add Income ")
    print("2. Add Expenses ")
    print("3. Check Balance ")

    op = int(input("Enter your choice : "))

    income_entry = {}
    expense_entry = None

    if op == 1:
        income_entry = add_income()
    elif op == 2:
        add_expense(expense_entry)
    elif op == 3:
        check_balance(income_entry)

    con = input(" Do you want to continue Y/N or y/n : ")




