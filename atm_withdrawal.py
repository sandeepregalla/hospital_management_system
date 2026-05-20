print(" **** ATM WITHDRAWAL ***   ")
print("")


user_password =int(input("Set The PIN : "))

if user_password :
    conform_password = int(input("Enter Conform Password :"))
    if conform_password== user_password :
        print("Password created Successfulyy")
        print("-------***---------")
        print(" DRAW THE AMOUNT ")
        user_amount = int(input("Enter The Amount :"))
        reuse_password = int(input("Enter The PIN :"))
        
        if user_password == reuse_password :
            print(f"your  withdrawal amount is : {user_amount}")
        else:
            print("WRONG PASSWORD PLEASE TRY AGAIN")    
    else:
         print("Not Match ")
         
            



 