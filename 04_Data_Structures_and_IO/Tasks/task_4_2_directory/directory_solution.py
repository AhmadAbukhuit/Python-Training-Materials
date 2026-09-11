def get_salary(employee_dict, emp_id):
    # First, safely get the employee. If not found, default to an empty dictionary {}
    employee = employee_dict.get(emp_id, {})
    
    # Then safely get the salary. If the dictionary is empty, default to "Not Found"
    return employee.get("salary", "Not Found")

def update_salary(employee_dict, emp_id, new_salary):
    # Check if the employee exists before trying to update to avoid a KeyError
    if emp_id in employee_dict:
        employee_dict[emp_id]["salary"] = new_salary