import json

number=int(input("enter any number:"))
filename= 'number.json'
with open('filename','w') as f:
    json.dump(number,f)

def read_number():
    with open('filename','r') as f:
        num= json.load(f)
        return f"Your fav number is {num}."

read_number()

def show_num():
    n_num=read_number()
    if n_num:
        print(n_num)
    else:
        n_num= int(input("enter a number: "))
        print(n_num)

show_num()