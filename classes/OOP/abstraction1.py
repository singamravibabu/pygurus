'''
Purpose:
1. Enforce Implementation
2. Polymorphism
3. Code Organization

Applications of ABCs and Polymorphism:
1. Web Frameworks: Django
2. Graphics and Game Develepment: Game Engines and Rendering Engines
3. Data Processing Pipelines: ETL Processes
4. Automated Testing: Test Frameworks
5. Financial Systems: Trading Platforms
6. Robotics: Control Systems
7. Machine Learning and AI: Model Implementations & Data Processing
8. Telecommunications
9. Content Management Systems
10. IoT systems
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine starting")

class Bike(Vehicle):
    def start(self):
        print("Bike engine starting")
        
car = Car()
car.start()

bike = Bike()
bike.start()