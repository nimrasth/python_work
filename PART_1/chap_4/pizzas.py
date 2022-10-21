# pizza
pizza= ['BBQ Chicken Pizza', 'Margherita Pizza', 'Cheese Pizza', 'Pepperoni Pizza']
for pizza in pizza:
    print (f"I like {pizza}")
print("Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various toppings. I really  love pizza!\n")


# animals
animal=['snake','crocodile', 'lizard']
for animal in animal:
    print(f"{animal}, is a reptile.")
print("These animals are most easily recognized by their dry & scaly skin.\n")


# slices
pizza= ['BBQ Chicken Pizza', 'Margherita Pizza', 'Cheese Pizza', 'Pepperoni Pizza', 'Hawaii Pizza']
print("The first three items of the list are:")
print(pizza[0:3])

print("\nThree items from the middle of the list are:")
print(pizza[1:4])
    
print("\nThe last three items of the list are:")
print(pizza[-3:])


# My Pizzas, Your Pizzas
friend_pizzas= pizza[:]
pizza.append('Meats Lover pizza')
friend_pizzas.append('Mushroom pizza')
print(f"\nMy favorite pizzas are: {pizza}")
print(f"\nMy friends favorite pizzas are: {friend_pizzas}")


# More Loops
for pizza in pizza:
    print(pizza)
print("\n")
for friend_pizzas in friend_pizzas:
    print(friend_pizzas)