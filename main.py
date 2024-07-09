#SIMPLE PYTHON DATABASE TO VIEW AND CHANGE EMPLOYEE DETAILS IN A TERMINAL BASE STYLE
#DOES NOT SUPPORT ADDING EMPLOYEE
import json


with open('employees.json') as employees:
    employee_json = json.load(employees)

class Employee:
    def __init__(self, name, emplid, salary=None, job_type=None):
        self.name = name
        self.emplid = emplid
        self.salary = salary
        self.job = job_type

        self.employee = employees

    #update the employee name
    def up_name(self, oldname, newname):
        for i in range(len(employee_json)):
            if oldname == employee_json[i]['name']:
                employee_json[i]['name'] = newname
                print('Name updated')
                main()
    #update the employee salary
    def up_salary(self, empid, salary):
        for i in range(len(employee_json)):
            if employee_json[i]['emp_num'] == empid:
                employee_json[i]['salary'] = salary
                print('Salary updated')
                main()
            else:
                print('Invalid employee id')
                main()
    #update the employee ID    
    def up_emplid(self, old_emp, newemplid):
        for i in range(len(employee_json)):
            if employee_json[i]['emp_num'] == old_emp:
                employee_json[i]['emp_num'] = newemplid
                print('ID updated')
                main()
            else:
                print('Invalid employee id')
                main()
    #update the employee job status   
    def up_jobtype(self, emplid, jobtype):
        for i in range(len(employee_json)):
            if employee_json[i]['emp_num'] == emplid:
                employee_json[i]['job_type'] = jobtype
                print('Job updated')
                main()
            else:
                print('Invalid employee id')
                main()

    #this will be the function you run first to see all current employees
    def load_emp(self):
        for i in range(1, len(employee_json)):
            print(f'{i}', employee_json[i])


#This will be the function to control the whole program, calling the menu etc
def main():
    quit = 0
    while quit != 1:
        print(
            """
            Use the load all employees Functions first

            1). Update Employee Name
            2). Update Employee salary
            3). Update Employee job type
            4). Load All Employee
            """
        )
        choice = input ("\nEnter choice: ")

        if choice == "1":
            search = input('Search for employee name: ')
            for i in range(len(employee_json)):
                if employee_json[i]['name'].lower() == search.lower():
                    print(f"Updating {employee_json[i]['name']} name")
                    change_name = input("Enter new name: ")
                    Employee(name=employee_json[i]['name'],emplid=employee_json[i]['emp_num']).up_name(employee_json[i]['name'],change_name)
                else:
                    print('Employee does not exist')
                    main()


        elif choice == "2":
            Found = True
            empnum = input('Enter employee number of employee: ')
            for i in range(len(employee_json)):
                if employee_json[i]['emp_num'] == empnum:
                    print(f"Updating {employee_json[i]['name']} salary\n")
                    new_sal = input('Enter new salary: ')
                    Employee(name=employee_json[i]['name'],emplid=employee_json[i]['emp_num']).up_salary(empnum,new_sal)
                else:
                    print('Employee does not exist')
                    main()


        elif choice == "3":
            print( '3 job roles [crew member supervisor manager]')
            empid  = input('Enter the employee number: ')

            for i in range(len(employee_json)):
                if employee_json[i]['emp_num'] == empid:
                    job_type = input('Enter job type: ')
                    if job_type.lower() in ['manager', 'supervisor', 'crew_member']:
                        Employee(name=employee_json[i]['name'],emplid=employee_json[i]['emp_num']).up_jobtype(empid, job_type)
                    else:
                        print( 'Job type not supported')
                        main

        #temp employee for load function
        elif choice == '4':
            Employee('demar', 5000, 7000, 'manager').load_emp()
            continue
        else:
            continue


main()