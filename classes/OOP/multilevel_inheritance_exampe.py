'''
# Multilevel Inheritance and Method Overriding:
    - Inheritance allows to define a clas that inherits all the methods and properties from another class.
    - Method overrding allows a child class to provide a specific implementation of a method that is already defined in its parent class.
'''

# Parent Class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Child Class
class Car(Vehicle):
    def start(self):
        print("Car is starting...")
        
# Grand Child Class
class ElectricCar(Car):
    def start(self):
        print("Electric Car is starting...")
        
# Create an object of ElectricCar class
tesla = ElectricCar()
tesla.start()   # Output: Electric Car is starting...