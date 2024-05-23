# Authself=Nonee Cano
# GitHub username: jovanecano
# Date: 05/22/2024
# Description:
"""This script defines the Employee class and a function that creates a dictionary of employees from the list of detials"""


class Employee:
    """A class Employees that represents an employee, gathers the following data for each
        name, id_number, salary, email_address"""

    def __init__(self, name, id_number, salary, email_address):
        # initializing the data members within our class Employees
        self.name = name
        self.id_number = id_number
        self.salary = salary
        self.email = email_address

    # using the get method to gather all the relevant data from the data members above
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id_number
    def get_salary(self):
        return self.salary
    def get_email_address(self):
        return self.get_email_address

def make_employee_dict(names, ids, salaries, emails):
    """creating a function taht will first create an empty dictionary then gather
        all relevant data from employee details using a for loop"""

    employee_dictionary = {}  #creating empty dictionary to store IDs as keys and values (name, salry, email_address)
    for i in range(len(names)):
        employee = Employee(names[i], ids[i], salaries[i], emails[i])
        employee_dictionary[ids[i]] = employee

    return employee_dictionary


#using example from assignment repo but printing all 3 in reverse order
#emp_names = ["Jean", "Kat", "Pomona"]
#emp_ids = ["100", "101", "102"]
#emp_sals = [30, 35, 28]
#emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
#result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
#print(result["102"].get_name()) #prints out Pomona
#print(result["101"].get_name()) #prints out Kat
#print(result["100"].get_name()) #prints out Jean

