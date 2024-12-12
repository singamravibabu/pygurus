# In Python, methods can be categorized into three types:
'''
1. Class Methods
2. Static Methods
3. Instance Methods
'''

## Instance Methods
'''
Operate on instances of the class.
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance Method
    def bark(self):
        print(f'{self.name} says woof!')

dog1 = Dog("Buddy", 9)
dog1.bark()


## Class Methods
'''
Operate on class iteself, not on instances.
'''
class Animal:
    species = "Mammal"
    
    def __init__(self, name):
        self.name = name
        
    # Class Method
    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

Animal.set_species("Reptile")
print(Animal.species)


### Static Methods
'''
Do not operate on instances or the class; they are utility functions related to the class.
'''

class MathUtils:
    @staticmethod
    def average(a, b):
        return a + b / 2
    
# Using static method
result = MathUtils.average(2, 1)
print(result)