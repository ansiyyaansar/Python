import os
import json

employees = {'count':0, 'employee_list':[]}

def clear():
    os.system("clear")

def save_file():
    with open('employees.json','w+')as file:
        json.dump(employees, file, indent=4)
        print("Json file created successfully!")


def display_details(emp):
    clear()
    if emp:
        print(f"Employee\n\tID: {emp['emp_id']}\n\tName: {emp['name']}\n\tAge: {emp['age']}\n\tPhone: {emp['phone']}\n\tExperience: {emp['experience']}\n\tGrade: {emp['grade']}")
    else:
        print("Employee details not available")

def add_employee():
    clear()
    flag=0
    while flag==0:
        try:
            emp_id = int(input("Enter employee id: "))
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            phone = int(input("Enter employee phone number: "))
            experience = int(input("Enter employee experience: "))
            grade = int(input("Enter employee grade: "))
            break
        except:
            print("invalid character")
    emp_obj ={
        'emp_id': emp_id,
        'name': name,
        'age': age,
        'phone': phone,
        'experience': experience,
        'grade': grade
    }
    employees['count']+=1
    employees['employee_list'].append(emp_obj)
    print(f"New Employee({emp_id}) added successfully")

def read_employee():
    clear()
    flag=0
    emp_id = int(input("Enter employee id: "))

    for emp in employees['employee_list']:
        if emp['emp_id'] == emp_id:
            flag=1
            print(f"Employee\n\tID: {emp['emp_id']}\n\tName: {emp['name']}\n\tAge: {emp['age']}\n\tPhone: {emp['phone']}\n\tExperience: {emp['experience']}\n\tGrade: {emp['grade']}")
            break
    if flag==0:
        print("Empoyee details not found")

def search_employee():
    clear()
    flag=0
    emp_id = int(input("Enter employee id: "))
    emp_obj = None
    for emp in employees['employee_list']:
        if emp['emp_id'] == emp_id:
            flag=1
            print(f"Employee\n\tID: {emp['emp_id']}\n\tName: {emp['name']}\n\tAge: {emp['age']}\n\tPhone: {emp['phone']}\n\tExperience: {emp['experience']}\n\tGrade: {emp['grade']}")
            break
            
    if flag==0:
        print("Empoyee details not found")

def update_employee():
    clear()
    flag=0
    emp_id = int(input("Enter employee id: "))
    for emp in employees['employee_list']:
        if emp['emp_id'] == emp_id:
            flag = 1
            while True:
                clear()
                field_no = int(input("Which field you want to update?\n\t1.Name\n\t2.Age\n\t3.Phone\n\t4.Experience\n\t5.Grade\n\t6.Back to Main\n\tEnter your option: "))
                if field_no == 1:
                    emp['name'] = input("Name: ")
                elif field_no == 2:
                    emp['age'] = int(input("Age: "))
                elif field_no == 3:
                    emp['phone'] = int(input("Phone: "))
                elif field_no == 4:
                    emp['experience'] = int(input("Experience: "))
                elif field_no == 5:
                    emp['grade'] = int(input("Grade: "))
                elif field_no == 6:
                    break
                else:
                    print('Enter a valid input')
            print(f"Employee\n\tID: {emp['emp_id']}\n\tName: {emp['name']}\n\tAge: {emp['age']}\n\tPhone: {emp['phone']}\n\tExperience: {emp['experience']}\n\tGrade: {emp['grade']}")
            break
    if flag == 0:
        print("Empoyee details not found")

def delete_employee():
    clear()
    emp_id = int(input("Enter employee id: "))
    flag = 0
    for emp in employees['employee_list']:
        if emp['emp_id'] == emp_id:
            display_details(emp)
            employees.remove(emp)
            print("Employee removed successfully")
            flag = 1
            break
    if flag == 0:
        print('Employee does not exists')

while True:
    try:
        print("\n__Options__\n1. Add Employee\n2. Display Employee\n3. Delete Employee\n4. Search Employee\n5. Update Employee\n6. Save file\n7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            read_employee()
        elif choice == 3:
            delete_employee()
        elif choice == 4:
            search_employee()
        elif choice == 5:
            update_employee()
        elif choice == 6:
            save_file()
        elif choice == 7:
            break
        else:
            print("--Invalid Option--")
    except:
        print("Invalid Options")
        raise
