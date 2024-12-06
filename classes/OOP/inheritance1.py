# child and parent class
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def speak(self):
        print(f"{self.name}, {self.color} in color is speaking")
        
class Dog(Animal):
    def speak(self):
        print(f"{self.name}, {self.color} in color is barking")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name}, {self.color} in color is meowing")
        
class Cow(Animal):
    def speak(self):
        print(f"{self.name}, {self.color} in color is mooing")
        
dog = Dog("Tommy", "Brown")
print(dog.speak())

cat = Cat("Kitty", "White")
print(cat.speak())