number = input("Enter the Marks List :").split()

num=[]

for i in number:
    if i not in num:
        num.append(i)
            
print(num)

num.sort()
print("asenting order :",num)

print("Highest Number :",max(num))

num.reverse()
print("desending order :", num)

print("Lowest Number  :", min(num))

