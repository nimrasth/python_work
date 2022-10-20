from restaurant import Restaurant
import random

res_3=Restaurant('trisara', 'nepalese')
print(res_3.describe_restaurant())




class Dice:

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):        
        print(random.randrange(1,self.sides))

print("\n")
x=range(10)   
for n in x:
    turn_1=Dice(20)
    turn_1.roll_die()

