# dictionary - we can store key value pair

# ordered, not allow duplicate values, changable

# Duplicate values will overwrite existing values

studentDetail = {
    "name":"Gowdham",
    "mobile":94584395,
    "address": "no:3, aaa street",
    "isActive": False
    }
print(studentDetail)
print(type(studentDetail))

print(studentDetail["mobile"])
print(len(studentDetail))

# dictionary with constructor

employee = dict(empId = "EMP001",empName = "demo user")
print(employee, type(employee))

# accessing

print(employee["empName"])

Employee_Name = employee.get("empName")
print(Employee_Name)


# keys()- it returns the keys in list
getKeys = employee.keys()
print(getKeys)

getValues = employee.values()
print(getValues)

employee["salary"] = 20000
employee["department"] = "demo department"

employee["salary"] = 55000
print(employee)

# items() -return each item in a dictionary, as tuples in a list.

getItems = employee.items()
print(getItems)





