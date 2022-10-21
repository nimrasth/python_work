'''
# pizza toppings
toppings = input("Enter your pizza topping: ")

while toppings != 'quit':
    print(f"{toppings} is added to your pizza")
    toppings = input("Enter your pizza topping: ")


# movie tickets
age = input("enter your age: ")
while age!= 'quit' :
    if int(age) < 3 :
        print("\nYour ticket is free.")
    elif int(age) > 3 and int(age)<12 :
        print("\nYour ticket price is $10.")
    else:
        print("\nYour ticket price is $15.")
    age = input("\nenter your age: ")

    
# movie tickets using active flag
    
active = True
while active:
    age = input("\nenter your age: ")
    if age=="quit":
        active= False
    elif int(age) < 3 :
        print("\nYour ticket is free.")
    elif int(age) >= 3 and int(age)<12 :
        print("\nYour ticket price is $10.")
    elif int(age)>=12 :
        print("\nYour ticket price is $15.")
    
'''

# movie tickets using break
while True:
    age = input("\nenter your age: ")
    if age=="quit":
        break
    elif int(age) < 3 :
        print("\nYour ticket is free.")
    elif int(age) >= 3 and int(age)<12 :
        print("\nYour ticket price is $10.")
    elif int(age)>=12 :
        print("\nYour ticket price is $15.")