n = int(input("Enter the Number: "))
sum = 0

# sum of numbers
for i in range(1,n+1):
    if i % 3 == 0:
        print("skippin:",i)
        sum  += 1 
               
print(sum)

#sum of even numbers

# for i in range(1,n+1):
#     if i % 2 ==0:
#         sum += i
# print(sum)
