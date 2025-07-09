ERROR_MESSAGE = "Provided value is not valid"
customer_balance_values = []
active_loan_balance_values = []
expense_values = []


def if_new_expense_available(if_new_expense):
    while True:
        if if_new_expense.lower() in ["yes", "ayo"]:
            answer = True
            return answer
        elif if_new_expense.lower() in ["no", "voch"]:
            answer = False
            return answer
        else:
            if_new_expense = input("Please answer with: yes / ayo / no / voch")


full_name = input("Please provide customer full name")

customer_balance = input("Please provide balance amount")
while not customer_balance.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    customer_balance = input("Please provide balance amount")
else:
    customer_balance = float(customer_balance)
    customer_balance_values.append(customer_balance)

expense = input("Please provide expense amount")
while not expense.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    expense = input("Please provide expense amount")
else:
    expense = float(expense)
    expense_values.append(expense)

active_loan_balance = input("Please provide active loan balance")
while not active_loan_balance.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    active_loan_balance = input("Please provide active loan balance")
else:
    active_loan_balance = float(active_loan_balance)
    active_loan_balance_values.append(active_loan_balance)

while customer_balance + active_loan_balance - expense > 0:
    if_new_expense = if_new_expense_available(input("Do you want to provide a new expense details? Yes/No"))
    if if_new_expense:
        expense = input("Please provide expense amount")
        while not expense.replace(".", "", 1).isdigit():
            print(ERROR_MESSAGE)
            expense = input("Please provide expense amount")
        else:
            expense = float(expense)
            expense_values.append(expense)
            # customer_balance_values.append(customer_balance)
            # active_loan_balance_values.append(active_loan_balance)
    if customer_balance - expense < 0:
        if customer_balance + active_loan_balance - expense < 0:
            print(f"Error: Dear {full_name}, you {expense} cannot be used")
            break
            # missed_amount = expense - initial_balance - active_loan_balance
            # used_balance = initial_balance
            # new_balance = 0
            # used_loan = active_loan_balance
            # new_loan_balance = 0
        else:
            # used_balance = initial_balance
            customer_balance = 0
            customer_balance_values.append(customer_balance)
            expense_values.append(expense)
            active_loan_balance = active_loan_balance + customer_balance - expense
            active_loan_balance_values.append(active_loan_balance)
            # used_loan = expense - initial_balance
            # print(f"Warning: Dear {full_name}, your loan balance is being used, new loan balance is {new_loan_balance}")
    else:
        # used_balance = expense
        customer_balance = customer_balance - expense
        customer_balance_values.append(customer_balance)
        expense_values.append(expense)
        active_loan_balance_values.append(active_loan_balance)
        # print(f"Dear {full_name}, after spending {expense} amount, your new balance is {new_balance}")

    for i in range(len(expense_values)):
        print(f"Balance No {i + 1}: {customer_balance_values[i]}"
              f"\nExpense No {i + 1}: {expense_values[i]}"
              f"\nLoan No {i + 1}: {active_loan_balance_values[i]}")
