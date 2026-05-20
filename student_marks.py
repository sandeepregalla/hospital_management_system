marks = []

for i in range(6):
    mark =int(input("Enter the Marks = "))
    marks.append(mark)
    

print("Student Marks :",marks)
print("Lowest Marks :",min(marks))
print("Highest Marks :",max(marks))
average = sum(marks)/len(marks)

print("Average Marks : " ,average)