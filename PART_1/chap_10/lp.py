# with open('PART_1/chap_10/learning_python.txt','r') as learning:
#     contents= learning.read()
#     x=contents.replace('Python', 'cat')
#     print(x)


from fileinput import filename


filename= 'guest.txt'

def guest_name(name):
   
    print(name)

name=input("enter your name: ")
guest_name(name)

with open(filename,'a') as f:
    f.write(name)
    
    print(f)
   

