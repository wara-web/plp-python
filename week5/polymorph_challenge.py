# Base class: Vehicle
class Vehicle:
    def move(self):
        pass


# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road "


# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"


# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water "


# Function to demonstrate polymorphism
def vehicle_action(vehicle):
    print(vehicle.move())


# Creating instances of each class
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Testing polymorphism
vehicle_action(my_car)   # Output: Driving on the road 
vehicle_action(my_plane) # Output: Flying in the sky ✈️
vehicle_action(my_boat)  # Output: Sailing on the water 







