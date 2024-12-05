# simple encapsulation example
class Car:
    def __init__(self):
        self.__updateSoftware()
    def drive(self):
        print('driving')
    def __updateSoftware(self):
        print('updating software')

redcar = Car()
# redcar.__updateSoftware() will not work
redcar.drive()              # works fine