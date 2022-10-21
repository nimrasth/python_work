'''
# infinity loop
a=2
while a>1:
    print (a)
    a+=2


# sandwiches
sandwich_orders= ['Chicken Sandwich', 'Egg Sandwich', 'Seafood Sandwich', 'Ham Sandwich', 'Grilled Chicken Sandwich']
finished_sandwiches=[]
while sandwich_orders:
    f_s= sandwich_orders.pop()
    print(f"I made your {f_s}")    
    finished_sandwiches.append(f_s)
print("\nThe finished sandwiches are: ")
for finished_sandwiches in finished_sandwiches:
    print (finished_sandwiches)
'''

# no pastrami
sandwich_orders= ['Chicken Sandwich', 'Pastrami', 'Egg Sandwich', 'Pastrami', 'Seafood Sandwich', 'Ham Sandwich', 'Grilled Chicken Sandwich','Pastrami']
print("The deli has run out of pastrami.")
finished_sandwiches=[]
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami') 
while sandwich_orders:
    f_s= sandwich_orders.pop()  
    finished_sandwiches.append(f_s)
print("\nThe finished sandwiches are: ")
for finished_sandwiches in finished_sandwiches:
    print (finished_sandwiches)
