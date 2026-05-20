expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choise = input("Enter Choise :")

    if choise == "1":
        name = input("Enter The Name : ")
        amount =input("Enter The Amount :")

        expenses.append({

            "name":name,
            "amount":amount

        })

        print("Expense Added successfully")
    elif choise =="2":
        print("\n Expenses List")

        for expense in expenses:
            print(expense["name"],"=",expense["amount"])

    elif choise == "3":

        total = 0

        for expense in expenses:
            total += float(expense["amount"])

        print("Total Expense:", total)  

    elif choise == "4":
        print("Exiting...")
        break
    else:
        print("invalid")                    