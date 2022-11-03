# # addition calculator
# print("\nEnter two numbers")
# print("press 'q' to quit")
# while True:
#     num_1= input("\nenter first number: ")
#     if num_1=='q':
#         break
#     num_2= input("Enter second number: ")
#     if num_2=='q':
#         break
#     try:
#         add= int(num_1) + int(num_2)
#     except ValueError:
#         print("please enter a number")
#     else:
#         print(add)


# # cats and dogs
# try:
#     with open('dogs.txt', encoding='utf-8') as f:
#         contents = f.read()
# except (FileNotFoundError):
#         print("file not found")
# else:
#     print(contents)


# silent Cats and Dogs
try:
    with open('dogs.txt', encoding='utf-8') as f:
        contents = f.read()
except (FileNotFoundError):
        pass
else:
    print(contents)


# the most impportant part of 9