
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))


if a > b and  a >c:
    print(f"Largest Number is  =" ,a)
elif b > a and b > c :
    print(f"Largest Number is =",b)
else:
    print("Largest Number is =",c)