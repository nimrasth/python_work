
# no users

user=['admin', 'alex', 'jaden', 'harry', 'William']
for person in user:
    if person=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {person.title()}, thank u for logging again! ")


user.clear()
if user==[]:
    print("\nwe need to find users.")




# checking usernames
current_users= ['ram', 'shyam', 'hari', 'shiva', 'gopal']
new_users= ['sita', 'gita', 'ram', 'shiva', 'parvati']
for person in new_users:
    if person.lower() in current_users:
        print("\n The username is already taken.")
    elif person.lower() not in current_users:
        print("\n This username is available.")


# ordinal numbers
ordinal_number=[1,2,3,4,5,6,7,8,9]
for number in ordinal_number:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")
    

    

