__Author__ = "noduez"

# 9-6冰淇淋小店
class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title()+' ' +self.cuisine_type)

    def open_restaurant(self):
        print("It's opening!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

class IceCreamStand(Restaurant):

    def __init__(self,name,cuisine_type='ice_cream'):

        super().__init__(name,cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nThe IceCreamStand's flavors: ")
        for fla in self.flavors:
            print(fla.title())

bigOne = IceCreamStand('The Big One')
bigOne.flavors = ['vanilla', 'chocolate', 'black cherry']

bigOne.describe_restaurant()
bigOne.show_flavors()


# 9-8权限 - 将实例用作属性
class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print('\nAdmin have these privileges: ')
        for privilege in self.privileges:
            print(privilege)

#9-7 管理员
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

class Admin(User):

    def __init__(self,first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()



admin = Admin('tom', 'alun')
# admin.show_privileges()
admin.privileges.show_privileges()


#9-9 电瓶
class Car():
   """A simple attempt to represent a car."""

   def __init__(self, manufacturer, model, year):
       """Initialize attributes to describe a car."""
       self.manufacturer = manufacturer
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       """Return a neatly formatted descriptive name."""
       long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
       return long_name.title()

   def read_odometer(self):
       """Print a statement showing the car's mileage."""
       print("This car has " + str(self.odometer_reading) + " miles on it.")

   def update_odometer(self, mileage):
       """
       Set the odometer reading to the given value.
       Reject the change if it attempts to roll the odometer back.
       """
       if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
       else:
           print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       """Add the given amount to the odometer reading."""
       self.odometer_reading += miles

class Battery():
   """A simple attempt to model a battery for an electric car."""

   def __init__(self, battery_size=60):
       """Initialize the batteery's attributes."""
       self.battery_size = battery_size

   def describe_battery(self):
       """Print a statement describing the battery size."""
       print("This car has a " + str(self.battery_size) + "-kWh battery.")


   def get_range(self):
       """Print a statement about the range this battery provides."""
       if self.battery_size == 60:
           range = 140
       elif self.battery_size == 85:
           range = 185

       message = "This car can go approximately " + str(range)
       message += " miles on a full charge."
       print(message)

   def upgrade_battery(self):
       """Upgrade the battery if possible."""
       if self.battery_size == 60:
           self.battery_size = 85
           print("Upgraded the battery to 85 kWh.")
       else:
           print("The battery is already upgraded.")


class ElectricCar(Car):
   """Models aspects of a car, specific to electric vehicles."""

   def __init__(self, manufacturer, model, year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """
       super().__init__(manufacturer, model, year)
       self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

