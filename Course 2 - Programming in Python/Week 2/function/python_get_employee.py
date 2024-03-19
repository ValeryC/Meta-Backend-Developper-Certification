# This is a simple example of how to get an employee from a list of employees using python
employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")] # list of employees

def get_employee(id): # function to get an employee
    for employee in employee_list: # loop through the list of employees
        if employee[0] == id: # if the employee id is found
            return {"id": employee[0], "name": employee[1], "department": employee[2]} # return the employee details

print('get_employee =', get_employee(12458)) # {'id': 12458, 'name': 'Paul', 'department': 'House Floor'}



employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

    # This function retrieves an employee's details from a dictionary using the employee's ID.
    # Parameters:
    # id (int): The ID of the employee.

    # Returns:
    # dict: A dictionary containing the employee's details (ID, name, and department).

    # Example:
    # >>> get_employee_from_dict(12458)
    # {'id': '12458', 'name': 'Paul', 'department': 'House Floor'}
def get_employee_from_dict(id):
    return employee_dict[id]


print('get_employee_from_dict =',get_employee_from_dict(12458)) # {'id': '12458', 'name': 'Paul', 'department': 'House Floor'}