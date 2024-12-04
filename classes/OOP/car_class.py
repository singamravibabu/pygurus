class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}")
        
    def __str__(self):
        return f"Default info: {self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Corolla", 2019)
car2 = Car("Honda", "Civic", 2018)
car3 = Car("Ford", "Fiesta", 2017)

print(car1)