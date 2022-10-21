'''
# rental car
rental_car=input("What kind of car would you like to rent?: ")
print(f"Let me see if I can find your {rental_car}.")


# restaurant seating
people=int(input("\nhow many people are there in your dinner group?: "))
if people > 8:
    print("You'll have to wait for your table.")
else:
    print("Your table is ready.")
    
'''

# multiples of 10
number= int(input("Enter a number: "))
if number % 10 ==0: 
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
