students =[
    {
    "name":"sandeep",
    "age":24,
    "marks":80
    },
    {
    "name":"vishwandh",
    "age":25,
    "marks":75
    },
    {
    "name":"vinodh",
    "age":22,
    "marks":80
    }
]

found =False

search = input("Search The Student Name :")

for student in students:
    if student["name"]==search:        
        print("student is found")
        print(student)
        found= True
if not found:
    print("student is not found")        
    