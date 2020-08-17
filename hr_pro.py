from datetime import datetime

class Employee:
    def __init__(self, name, age, salary, employment_year ):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def __str__(self):
        msg = f'''
        Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}
        '''
        return msg

    def get_working_years(self):
        return 2020 - self.employment_year


class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return (self.bonus_percentage * self.salary/100)

    def __str__(self):
        return f'''
        Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()},  Bonus: {self.get_bonus()}
        '''


def main():
    list_employees = []
    list_managers = []
    while True:
        entry = input("""
        *************** Welcome to HR Pro 2020 ***************

        Options:

        1. Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit

        What would you like to do? """)

        if entry == "1":
            print("Employees:")
            for employees in list_employees:
                print(employees)

        elif entry == "2":
            print("Managers: ")
            for managers in list_managers:
                print(managers)

        elif entry == "3":
            print("Please fill the employee information:")
            name = input("Name:")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year = int(input("Employement year: "))

            list_employees.append(Employee( name, age, salary, employment_year ))

            print("Employee added succesfully")


        elif entry == "4":
            print("Please fill the manager information:")
            name = input("Name:")
            age = input("Age: ")
            salary = int(input("Salary: "))
            employment_year = int(input("Employement year: "))
            bonus_percentage = int(input("Bonus Percentage: "))

            list_managers.append(Manager( name, age, salary, employment_year, bonus_percentage))

            print("Manager added succesfully")

        elif entry == "5":
            return False

        else:
            print("Not a valid entry!")

if __name__ == '__main__':
    main()
