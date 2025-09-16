import os

EMPLOYEE_FILE = "employees.txt"
EMPLOYEE_ID_NUMBER = "employee_id.txt"

id_number = 1000
employees = []


def get_next_id_number():
    global id_number
    id_number += 1
    employee_number = id_number
    return employee_number

def create_employee(name, age, title, id_number=None):
    if not id_number:
        id_number = get_next_id_number()
    
    emp = {"id": id_number,
           "name":name,
           "age":age,
           "title":title}
    return emp

def print_employee(emp):
    print(f"ID: {emp['id']}")
    print(f"Name: {emp['name']}")
    print(f"Age: {emp['age']}")
    print(f"Title: {emp['title']}")

def check_for_age(age_string):
    if not age_string.isdigit():
        return False
    
    if 1 <= int(age_string) <= 120:
        return True
    
    return False

def save_employees():
    with open(EMPLOYEE_ID_NUMBER, "w") as f:
        f.write(str(id_number))

    with open(EMPLOYEE_FILE, "w", encoding="utf-8") as f:
        for emp in employees:
            id_num = emp["id"]
            name = emp["name"]
            age = emp["age"]
            title = emp["title"]

            f.write(f"{id_num},{name},{age},{title}\n")

def load_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "w", encoding="utf-8") as f:
            pass
    else:
        with open(EMPLOYEE_FILE, "r", encoding="utf-8") as f:
            for employee_text in f.readlines():
                id_num, name, age, title = employee_text.strip().split(",")
                emp = create_employee(name, int(age), title, int(id_num))
                employees.append(emp)
                

    if not os.path.exists(EMPLOYEE_ID_NUMBER):
        with open(EMPLOYEE_ID_NUMBER, "w") as f:
            pass
    else:       
        with open(EMPLOYEE_ID_NUMBER, "r") as f:
            num = f.read()
            global id_number
            id_number = int(num)
    


load_employees()
while True:
    print("1. Create new employee")
    print("2. List all employees")
    print("0. Quit")

    choice = input("Make a choice: ")

    if choice == "1":
        name = input("Give name: ")
        age = input("Give age: ")
        if check_for_age(age):
            age = int(age)
            title = input("Give title: ")
            new_employee = create_employee(name, age, title)
            employees.append(new_employee)

        print("Invalid age, start over noob!")

    elif choice == "2":
        for emp in employees:
            print_employee(emp=emp)

    elif choice == "0":
        break

    else:
        print("Invalid input!")

save_employees()