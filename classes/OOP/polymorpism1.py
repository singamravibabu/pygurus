class Bird:
    def fly(self):
        print("Bird is flying")
        
class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly but can swim")

# polymorphism in action
def make_it_fly(bird):
    bird.fly()
    
sparrow = Bird()
penguin = Penguin()

make_it_fly(sparrow)        # Output: Bird is flying
make_it_fly(penguin)        # Output: Penguin can't fly but can swim