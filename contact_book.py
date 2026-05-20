contacts = {}

#add contact
def add_contact():
    name =input("Enter The Name: ")
    phone=int(input("Enter The Phone Number:"))
    contacts[name]=phone
    print("Contact Added ")
# viwe total contacts
def view_contacts():
    if not contacts:
        print("No Contacts Found!\n")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")
        print()   
#search contacts
def search_contacts():
    name = input("Enter Name To Search Contact :")

    if name in  contacts:
        print(f"name:{name} | phone :{contacts[name]}")
    else:
        print("Contact Not found!")

#update contacts
def update_contacts():
    name =input("Enter Name To Update :")
    
    if name in contacts:
        new_phone =input("Enter New Phone Number :")
        contacts[name]=new_phone
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")    
    
def delete_contacts():
    name = input("Enter Delete To Name :")
    if name in contacts:
        del contacts[name]
        print("Deleted Contact Successfully")


while True:
    print("----CHOISE------")
    print("1.Add Contacts")
    print("2.View Contacts")
    print("3.Search Contacts")
    print("4.update Contacts")
    print("5.delete Contacts")


    choise =input("Enter Your Choise :")
    if choise=="1":
        add_contact()
    elif choise=="2":
        view_contacts()
    elif choise=="3":
        search_contacts()
    elif choise=="4":
        update_contacts()
    elif choise=="5":
        delete_contacts()            
    else:
        print("Invalid Choise")        




