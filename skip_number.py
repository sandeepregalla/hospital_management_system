n = int(input("Enter the Number :"))
count =0

for i in range(1,n+1):
    if i % 5 ==0:
        print("skipping",i)
        continue
    print("adding:",i)
    count+=i
print("sum :",count)    