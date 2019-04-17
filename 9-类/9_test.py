__Author__ = "noduez"

#9-1 餐馆
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title()+' ' +self.cuisine_type)

    def open_restaurant(self):
        print("It's opening!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant('Da fan dian', 'haidilao')
restaurant.describe_restaurant()
restaurant.open_restaurant()


#9-2 三家餐馆
restaurant1 = Restaurant('A','a')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('B','b')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('C','c')
restaurant3.describe_restaurant()


#9-3 User
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() +' '+ self.last_name.title())

    def greet_user(self):
        print('How are you doing?')

    def increment_login_attemps(self):
        self.login_attempts += 1

    def rest_login_attempts(self):
        self.login_attempts = 0


user1 = User('joey','cbianni')
user1.describe_user()
user1.greet_user()
user2 = User('dsdf', 'csfs')
user2.describe_user()
user2.greet_user()

#9-4 就餐人数
restaurant4 = Restaurant('D','a')
print('There hava '+str(restaurant4.number_served)+ ' prople eated')
restaurant4.number_served = 2
print('There hava '+str(restaurant4.number_served)+ ' people eated')

restaurant4.set_number_served(7)
print('There hava '+str(restaurant4.number_served)+ ' people eated')

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

#尝试登录次数
user3 = User('Anf','Dds')
print("user's attempsts times: "+str(user3.login_attempts))
user3.increment_login_attemps()
print("user's attempsts times: "+str(user3.login_attempts))
user3.increment_login_attemps()
print("user's attempsts times: "+str(user3.login_attempts))

user3.rest_login_attempts()
print("user's attempsts times: "+str(user3.login_attempts))
