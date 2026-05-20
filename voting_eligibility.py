print("--------* CHECK YOUR VOTE ELIGIBILITY *-------")

age = int(input("Enter Your Age : "))

if age > 18 :
    print("Your Eligible For Vote")
elif age ==18:
    print("You just become eligible to vote ")
    
else:
    print(f"you are a {age} years old  not eligible to  vote ")


