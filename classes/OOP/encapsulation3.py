# encapsulation: private attribute
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def display(self):
        print(self.name)
        print(self.__age)
        
s1 = Student("John", 23)
print(s1.name)
print(s1.__age)


