print("*********Welcome To Hospital Management System***********")

import datetime
import csv
import os

FILE_NAME ="hospitalmanagement.csv"


#create file

def create_file():

    try:
        file =open(FILE_NAME,"x",newline="")
        writer =csv.writer(file)

        writer.writerow([
            "patient_id",
            "patient_name",
            "gendar",
            "date_of_birth",
            "age",
            "phone_number",
            "blood_group",
            "room_number",
            "status",
            "created_date"
        ])

        file.close()

    except FileExistsError:
        pass


#generate patient id

def genarate_id():

    try:

        file =open(FILE_NAME,"r")
        reader =csv.reader(file)
        next(reader)
        last_row =None

        for row in reader:
            last_row=row

        file.close()
        if last_row==None:
            return 101
        return int(last_row[0])+1
       
    except:
        return 101


#add patients details

def add_patients_details():

    patient_id = genarate_id()

    date =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    patient_name =input("Enter The Patiens Name : ")
    gendar =input("Enter The Patiens Gendar : ")
    date_of_birth =input("Enter The Patiens Data Of Birth : ")
    age =input("Enter The Patiens Age : ")
    phone_number =input("Enter The Phone Number : ")
    blood_group =input("Enter The patient Blood Group: ")
    room_number=input("Enter The Room Number: ")
    status=input("Enter The patient Status: ")

    file =open(FILE_NAME,"a",newline="")

    writer = csv.writer(file)

    writer.writerow([
        patient_id,
        patient_name,
        gendar,
        date_of_birth,
        age,
        phone_number,
        blood_group,
        room_number,
        status,
        date
    ])

    file.close()

    print("Patients Details Added Successfully",patient_id)


#view all patient details

def view_patient_details():

    file =open(FILE_NAME,"r")

    reader =csv.reader(file)

    print("\n========== Patients Details ==========\n")

    for row in reader:
        print(row)

    file.close()


#search patients records

def search_patients_details():

    search_patiens= input("Enter The Patiens Name: ")

    file =open(FILE_NAME,"r")

    reader =csv.reader(file)

    next(reader)

    found =False

    for row in reader:

        if row[1].lower()==search_patiens.lower():

            print("\nPatient Found")
            print(row)

            found=True

    if not found:
        print("No! Patiens on The Name")

    file.close()


#edit patient details

def edit_patient_details():

    patient_id = input("Enter Patient ID To Edit : ")

    updated_data = []

    found = False

    file = open(FILE_NAME,"r")

    reader = csv.reader(file)

    header = next(reader)

    updated_data.append(header)

    for row in reader:

        if row[0] == patient_id:

            found = True

            print("Old Data :",row)

            patient_name =input("Enter New Patiens Name : ")
            gendar =input("Enter New Gendar : ")
            date_of_birth =input("Enter New Date Of Birth : ")
            age =input("Enter New Age : ")
            phone_number =input("Enter New Phone Number : ")
            blood_group =input("Enter New Blood Group : ")
            room_number=input("Enter New Room Number : ")
            status=input("Enter New Status : ")

            date =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            row = [
                patient_id,
                patient_name,
                gendar,
                date_of_birth,
                age,
                phone_number,
                blood_group,
                room_number,
                status,
                date
            ]

        updated_data.append(row)

    file.close()

    file = open(FILE_NAME,"w",newline="")

    writer = csv.writer(file)

    writer.writerows(updated_data)

    file.close()

    if found:
        print("Patient Details Updated Successfully")
    else:
        print("Patient ID Not Found")


#delete patient details

def delete_patient_details():

    patient_id = input("Enter Patient ID To Delete : ")

    updated_data = []

    found = False

    file = open(FILE_NAME,"r")

    reader = csv.reader(file)

    header = next(reader)

    updated_data.append(header)

    for row in reader:

        if row[0] != patient_id:

            updated_data.append(row)

        else:
            found = True

    file.close()

    file = open(FILE_NAME,"w",newline="")

    writer = csv.writer(file)

    writer.writerows(updated_data)

    file.close()

    if found:
        print("Patient Deleted Successfully")
    else:
        print("Patient ID Not Found")


#create file first

create_file()


#main menu

while True:

    print("\n========= Hospital Management System =========")

    print("1. Add Patient Details")
    print("2. View Patient Details")
    print("3. Search Patient Details")
    print("4. Edit Patient Details")
    print("5. Delete Patient Details")
    print("6. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        add_patients_details()

    elif choice == "2":
        view_patient_details()

    elif choice == "3":
        search_patients_details()

    elif choice == "4":
        edit_patient_details()

    elif choice == "5":
        delete_patient_details()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")