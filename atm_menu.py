
print("--------* WELCOME *------")
print("   ")
print("        SET ATM PIN      ")
print("   ")

user_pin = int(input("Set Your PIN :"))
conform_pin = int(input("Conform Your PIN :"))


if user_pin == conform_pin :
    print("PIN Created Successfully")
    
    balance =0
    
    while True :
        print("\n ----* MENU *-----")
        print("ENTER PIN ==> Check Balance")
        print("1.Deposit Money")
        print("2.Draw The Money")
        print("3.Exit")
        
        options = int(input("Select The Above Options :"))
        
        if options == user_pin:
           print(f"Your Total Balance Is :{balance}")
           if balance == 0:
               print("Please Deposit Money 😒")
           
        elif options == 1:
            deposit_money =int(input("Enter The Money : "))
            take_pin =int(input("ENTER PIN : "))
            if take_pin== user_pin :                
                balance += deposit_money
                print(f"Your Deposited Money Is :{deposit_money} and TOTAL IS :{balance}")
            else:
                print("WRONG PIN 👎")    
        elif options == 2:
            draw_money = int(input("Enter The Money : "))
            taken_pin = int(input("ENTER PIN : "))
            if draw_money <= balance and taken_pin == user_pin:
                balance -= draw_money
                print(f"Your Draw The Money Is :{draw_money} and Total is :{balance}")
            else:
                print("insufficient")
                            
        elif options == 3:
            print("Thank You 🙏 ")
            break      
           
           
        else:
            print("INVALID!👎")   
        
    