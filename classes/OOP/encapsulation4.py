# encapuslation4.py: 2 private attributes, 2 public attributes
class Car:
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
        print(self.__name)
        
    def setMaxSpeed(self, speed):
        self.__maxspeed = speed
        
    def setName(self, name):
        self.__name = name
        
redcar = Car()
redcar.drive()
redcar.setName("Ferrari")
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
redcar.__maxspeed = 400
redcar.drive()
