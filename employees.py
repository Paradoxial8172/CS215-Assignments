
class Employee:
    def __init__(self, last_name: str, salary: float):
        self.last_name = last_name
        self.salary = salary

    def get_last_name(self):
        return self.last_name
    
    def get_salary(self):
        return self.salary

employee_list = []

def sort_employees_list(employee_list: list):
    n = 0
    for employee in employee_list:
        print(f"Employee {n+1} Last Name: {employee_list[n].get_last_name()}\nSalary: ${employee_list[n].get_salary()}")
        n += 1
    
def create_employees(k:int):
    for i in range(1, k+1):
        last_name = input(f"Enter the last name for employee {i}? ")
        salary = float(input(f"What is their average salary? $"))
        employee_list.append(Employee(last_name, salary))
    
    print("\tEmplpoyee Information:")
    sort_employees_list(employee_list)
    
def main():
    employee_count = int(input("How many employees will you have? "))
    create_employees(employee_count)

main()



