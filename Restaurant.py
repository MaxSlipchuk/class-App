class Restaraunt():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_retaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open")
    
    def set_number_served(self, count_visitor):
        self.number_served = count_visitor
    
    def increment_number_served(self, visitor):
        if visitor >= 1:
            self.number_served += visitor
        else:
            print("Error")
            

restaurant = Restaraunt("sisi", "italian")
restaurant.describe_retaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.number_served = 50
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
print(restaurant.number_served)
