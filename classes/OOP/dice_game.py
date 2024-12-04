# object composition
from dice import Die, Dice

num_dice = int(input("Enter the number of dice: "))
dice = Dice()

for i in range(num_dice):
    die = Die()             # Create a new Die object in each iteration
    dice.addDie(die)        # Add the Die object to the Dice object

dice.rollAll()
for die in dice.list:
    print(die.value)