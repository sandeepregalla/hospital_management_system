
while True:

    A = int(input("Enter the First Number :"))
    B = int(input("Enter the Second Number :"))
    C = ["+","/","*","%","-"]
    D = input(f"Seclect The Oparater {C} : ")

    if(D=="+"):
        print(A+B)
    elif(D=="-"):
        print(A-B)

    elif(D=="*"):
        print(A*B)

    elif(D=="%"):
        print(A%B)

    elif(D=="/"):
        print(A/B)
        

