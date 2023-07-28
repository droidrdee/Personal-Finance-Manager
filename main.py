# Personal Finance Manager

class Personal_finance_manager:
    def __init__(self):
        self.balance = 0
        self.income_transactions = []
        self.expense_transactions = []

    def add_income(self, amount, source):
        self.balance += amount
        self.income_transactions.append({'amount': amount, 'source':source})

    def add_expense(self, price, product):
        self.balance -= price
        self.expense_transactions.append({'price':price, 'product':product})

    def balance(self):
        return self.balance

    def transactions(self):
        print("Income Transactions:")
        for income in self.income_transactions:
            print(f"{income['source']}: +${income['amount']}")
        print("\nExpense Transactions:")
        for expense in self.expense_transactions:
            print(f"{expense['product']}: -${expense['price']}")


def main():

    pfm = Personal_finance_manager()

    while True:

        print("\n","------- MENU ------- ")
        print("1. Add Income ")
        print("2. Add Expense")
        print("3. View Balance ")
        print("4. Show Transactions ")
        print("5. Exit")

        ch = int(input("Enetr your choice : "))

        if ch == 1:
            amount = int(input("Enter amount of income : "))
            source = input("Enter source of income : ")
            pfm.add_income(amount, source)

        elif ch == 2:
            price = int(input("Enter price of expense : "))
            product = input("Enter the product name : ")
            pfm.add_expense(price, product)

        elif ch == 3:
            print("Your current remaining balance is : ",pfm.balance,"\n")

        elif ch == 4:
            pfm.transactions()

        elif ch == 5:
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()