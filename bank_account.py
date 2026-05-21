# class BankAccount:
    
#     def __init__(self,accountNo,accountName,IFCcode,balance):
#         self.accountNo=accountNo
#         self.accountName=accountName
#         self.IFCcode=IFCcode
#         self.balance=balance
#     def withdraw(self,amount):
#         self.balance -=amount
#     def deposite(self,amount):
#         self.balance +=amount
#     def checkbalance(self):
#         print(self.balance)    
# object1 =BankAccount(1235486545,"sandeep",'DBKoo053',50000)
# object1.withdraw(20000)
# object1.checkbalance() 
# object1.deposite(50000)
# object1.checkbalance()  



# class Person:
#   lastname = "Jackson"

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Emil")
# p2 = Person("Tobias")
# Person.lastname = "Hansen"
# print(p1.lastname)

class Person:
        
    def __init__(self, name):
        self.name = name
        self.lastname ="sandeep"	
    def printname(self):
        print(self.name)
        print(self.lastname)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()
