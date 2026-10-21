# 1. Base Grandparent Class
class Vehicle:
    def turn_on(self):
        print("🔑 Vehicle system activated.")

# 2. Hierarchical Step: Two classes inherit from Vehicle
class Car(Vehicle):
    def cruise(self):
        print("🚗 Cruising smoothly down the street.")

class Truck(Vehicle):
    def haul_load(self):
        print("🚛 Hauling heavy cargo.")

# 3. Multiple Step: One child class inherits from BOTH Car and Truck
class HybridTruck(Car, Truck):
    def eco_mode(self):
        print("🔋 Running on electric power.")

# --- Using the Hybrid Class ---
my_vehicle = HybridTruck()

my_vehicle.turn_on()    # Inherited from Grandparent (Vehicle)
my_vehicle.cruise()     # Inherited from Parent 1 (Car)
my_vehicle.haul_load()  # Inherited from Parent 2 (Truck)
my_vehicle.eco_mode()   # Its own method