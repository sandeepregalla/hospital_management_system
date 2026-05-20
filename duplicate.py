# numbers = [1,23,2,2,55,2,]

# unique = list(set(numbers))


# print(unique)

numbers = input("Enter the List Numbers : ").split()

num = []

for i in numbers:
    if i not in  num:
        num.append(i)
print(num)        