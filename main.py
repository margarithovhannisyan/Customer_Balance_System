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

active_loan_balance = input("Please provide active loan balance")
while not active_loan_balance.replace(".", "", 1).isdigit():
    print(ERROR_MESSAGE)
    active_loan_balance = input("Please provide active loan balance")
else:
    active_loan_balance = float(active_loan_balance)

while True:
    active_loan_balance_values.append(active_loan_balance)
    customer_balance_values.append(customer_balance)
    expense = input("Please provide expense amount")
    while not expense.replace(".", "", 1).isdigit():
        print(ERROR_MESSAGE)
        expense = input("Please provide expense amount")
    else:
        expense = float(expense)
        expense_values.append(expense)
    if expense <= customer_balance:
        customer_balance = customer_balance - expense
    elif expense <= customer_balance + active_loan_balance:
        active_loan_balance = active_loan_balance + customer_balance - expense
        customer_balance = 0
    else:
        missed_amount = expense - active_loan_balance - customer_balance
        customer_balance = 0
        active_loan_balance = 0
        print(f"Balance and Loan limits are met, you still need {missed_amount} to cover")
        break
    if not if_new_expense_available("Do you want to provide a new expense? (yes/no): "):
        break

customer_balance_values.append(customer_balance)
active_loan_balance_values.append(active_loan_balance)
expense_values.append(0)

for i in range(len(expense_values)):
    print(f"Balance No {i + 1}: {customer_balance_values[i]}"
          f"\nLoan No {i + 1}: {active_loan_balance_values[i]}"
          f"\nExpense No {i + 1}: {expense_values[i]}")
