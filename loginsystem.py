print("sign in ")

user_name = str(input("Enter the Name :"))
user_password =str(input("Enter the password :"))

if user_name and user_password :
    print("successfully created Account")
    print("****************")
    print("Please Login")
    set_user = input("Enter the user name :")
    set_user_password =input("Enter the user password :")
    
    if user_name == set_user and user_password == set_user_password :
        print("Login Successfuly")
    else:
        print("Login Faild")
else:
    print("Entered  Invalid")         
         


