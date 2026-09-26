def get_salary(employee_dict, emp_id):

    #     employee_dict = {
    #     "emp_01": {"name": "Alice", "salary": 85000},
    #     "emp_02": {"name": "Bob", "salary": 72000},
    # }
    
    employee = employee_dict.get(emp_id, {})

    # employee = {"name": "Alice", "salary": 85000}

    emp_salary = employee.get("salary", "Not Found")

    # emp_salary = 85000

    return emp_salary

    # return employee.get("salary", "Not Found")


def update_salary(employee_dict, emp_id, new_salary):

    if emp_id in employee_dict:
        employee_dict[emp_id]["salary"] = new_salary


db = {
    "emp_01": {"name": "Alice", "salary": 85000},
    "emp_02": {"name": "Bob", "salary": 72000},
}

salray = get_salary(db, "emp_03")
print(f"{salray}")
