'''
Using @property decorator to create a getter method
Using @property decorator to create a setter method
'''

class Circle:
    def __init__(self, radius):
        self.__radius = radius   # make it private
        
    @property   # getter method
    def radius(self):
        return self.__radius

    @radius.setter   # setter method
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value
    
circle = Circle(3)
print(circle.radius)
circle.radius = 5
print(circle.radius)