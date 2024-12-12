'''
# The super() Function:
The super() function is used to call methods of a parent class.
'''

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        
# Creating an Employee object
emp = Employee("Anand", 30, "E12345")
print(f"Name: {emp.name}, Age: {emp.age}, Employee ID: {emp.employee_id}")

'''
`super()` allows you to access methods of the parent class.
This is helpful when you want to extend or modify the parent class behavior.
'''