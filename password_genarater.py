import random 
import string

# otp =""

# password = string.digits

# for i in range(0,6):
#     otp +=random.choice(password)
# print(otp)    

while True:
    password =""

    char = string.digits+string.ascii_letters
    lenght = int(input("Enter The Length of Password (1 to 10) :"))

    for i in range(lenght):
        password +=random.choice(char)
    print(password)    