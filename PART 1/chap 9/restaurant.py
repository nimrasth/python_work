# restaurant
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return (f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        return (f"{self.restaurant_name} is open!")

# res_1 = Restaurant('Lavie Garden', 'nepalese')
# res_2 = Restaurant('Carpe Diem Lounge & Bakery', 'nepalese')
# print(res_1.describe_restaurant())
# print(res_1.open_restaurant())
# print(res_2.describe_restaurant())
# print(res_2.open_restaurant())


# class IceCreamStand(Restaurant):


#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)

    
       
#         self.flavors= flavors

#     def dis_flavors(self):
#         return f"The flavor is {self.flavors}"
    
# ice_1=IceCreamStand('Jasper', 'Chinese', 'Chocolate')
# print(ice_1.dis_flavors())


# # user
# class User:

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email= first_name + '.' + last_name + "@abc.com"
    
#     def describe_user(self):
#         info= f"{self.first_name} {self.last_name} is {self.age} years old and email id is {self.email}"
#         return info

#     def greet_user(self):
#         return f"Hello {self.first_name}"

# user_1=User('Ram', 'Shrestha', 40)
# user_2=User('Shyam', 'Pradhan', 50)
# # user_3=User('Hari', 'Kayastha', 30)
# # user_4=User('Gopal', 'KC', 60)

# print("\n")
# print(user_1.describe_user())
# print(user_1.greet_user())

# print(user_2.describe_user())
# print(user_2.greet_user())

# # print(user_3.describe_user())
# # print(user_3.greet_user())

# # print(user_4.describe_user())
# # print(user_4.greet_user())

# class Admin(User):

#     def __init__(self, first_name, last_name, age, privileges):
#         super().__init__(first_name, last_name, age)

#         self.privileges= privileges

#     def  show_privileges(self):
#         print(f"\nThe list of privileges of {self.first_name} {self.last_name} are: ")
#         for p in self.privileges:
#             print(p)
# p_msg=[ "can add post", "can delete post", "can ban user"]
# admin=Admin('Ayush','Shrestha',50,p_msg)
# admin.show_privileges()


# class Privileges:

#     def __init__(self, privileges):
#         self.privileges= privileges

#     def  show_privileges(self):
#         print(f"\nThe list of privileges of are: ")
#         for p in self.privileges:
#             print(p)

# p_msg=[ "can add post", "can delete post", "can ban user"]
# admin=Privileges(p_msg)
# admin.show_privileges()