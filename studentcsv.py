import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name", "Age", "City"])
writer.writerow(["Sandeep", 22, "Khammam"])
writer.writerow(["Rahul", 21, "Hyderabad"])

file.close()