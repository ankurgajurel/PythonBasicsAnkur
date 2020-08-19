class Restaurant():

    def __init__(self, restaurant_name, restaurant_address):
        self.Name = restaurant_name
        self.Address = restaurant_address

    def describe_restaurant(self):
        print (self.Name + " is located at " + self.Address)

    def open_restaurant(self):
        print("Now " + self.Name + " is OPEN")

R1 = Restaurant("'Trishara'", 'Baneshwor')

R1.describe_restaurant()
R1.open_restaurant()
