import csv
import datetime

FILE_NAME ="expenses.csv"

#Create Expenses File
def create_file():
    try:
        file =open(FILE_NAME,"x",newline="")
        writer = csv.writer(file)
        writer.writerow(["Date","Catagory","Title","Amount"])
        file.close
    except FileExistsError:
        pass    
def add_expense():

    
    catagory =input("Enetr Catagory : ")
    title=input("Enter Expense Title :")
    amount= float(input("Enter The Amount: "))
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    file =open(FILE_NAME,"a",newline="")
    writer =csv.writer(file)
    writer.writerow([date,catagory,title,amount])
    file.close
    print("Expense Added Successfully")

def view_file():

    file =open(FILE_NAME,"r")
    reader = csv.reader(file)
    print("\n Expense List ")

    for row in reader:
        print(row)

    file.close()

def total_expense():
    total= 0

    file =open(FILE_NAME,"r")
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += float(row[3])       

    file.close()
    print("Total is :",total)

    
def search_expense():

    search = input("Search catagory Name :")
    file = open(FILE_NAME,"r")

    reader = csv.reader(file)
    next(reader)
    found =False

    for row in reader:
        if row[1].lower()==search.lower():
            print(row)
            found=True
    if not found:
        print("No Expense Found")
    file.close()

def menu():

    create_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Search Category")
        print("5. Exit")

        choice = input("Enter The Choice :")

        if choice == "1":
            add_expense()

        elif choice =="2":
            view_file()
        elif choice=="3":
            total_expense()

        elif choice=="4":
            search_expense()
        elif choice =="5":
            print("Good Bye")
            break
        else:
            print("invalid choice")                               
menu()