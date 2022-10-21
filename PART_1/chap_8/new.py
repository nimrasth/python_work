# sandwiches
def sandwich(*item):
    print("\nThe ordered sandwiches are:")
    for sandwi in item:
        print(sandwi)
sandwich('ham','chicken','tuna')


# user profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
my_profile = build_profile('Nimra', 'Shrestha', location='satdobato', field='computer')
print("\n")
print(user_profile)
print(my_profile)


# cars
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer_name']= manufacturer
    car_info['model_name'] = model
    return car_info
car_profile= make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"\n{car_profile}")



# printing modules
def user(name, age):
    print(f"\n{name} is {age} years old.")

