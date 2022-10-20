# # number served
# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served=0

#     def describe_restaurant(self):
#         return (f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         return (f"{self.restaurant_name} is open!")

#     def set_number_served(self, no_cus):
#         self.number_served = no_cus
    
#     def read_cus(self):
#         print(self.number_served)
    
#     def increment_number_served(self,num):
#         a= self.number_served + num 
#         self.number_served = a

# res_1= Restaurant('Lavie Garden', 'nepalese')

# print(res_1.describe_restaurant())
# print(res_1.open_restaurant())

# res_1.read_cus()
# res_1.set_number_served(5)
# res_1.read_cus()
# res_1.increment_number_served(2)
# res_1.read_cus()



# login attempts

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email= first_name + '.' + last_name + "@abc.com"
        self.login_attempts = 0
    
    def describe_user(self):
        info= f"{self.first_name} {self.last_name} is {self.age} years old and email id is {self.email}"
        return info

    def greet_user(self):
        return f"Hello {self.first_name}"

    def increment_login_attempts(self):
        self.login_attempts+=1 
        print(self.login_attempts)

    def reset_login_attempts(self): 
        self.login_attempts = 0
        print(self.login_attempts)

user_1=User('Ram', 'Shrestha', 40)

print("\n")
print(user_1.describe_user())
print(user_1.greet_user())
user_1.increment_login_attempts()
user_1.reset_login_attempts()

