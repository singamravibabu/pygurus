# parent and child class: parent class named Car and child class named BMW
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def start(self):
        print(f"{self.name}, {self.color} in color is starting")
        
    def stop(self):
        print(f"{self.name}, {self.color} in color is stopping")

class BMW(Car):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model
        
    def start(self):
        print(f"{self.name}, {self.color} in color is starting with model {self.model}")
        
    def stop(self):
        print(f"{self.name}, {self.color} in color is stopping with model {self.model}")