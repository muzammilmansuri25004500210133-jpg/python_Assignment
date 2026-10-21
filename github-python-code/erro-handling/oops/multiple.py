# Grandparent Class
class Vehicle:
    def start_engine(self):
        print("🚗 Engine started!")

# Parent Class (Inherits from Vehicle)
class Car(Vehicle):
    def drive(self):
        print("🛣️ Driving on the road...")

# Child Class (Inherits from Car)
class ElectricCar(Car):
    def charge_battery(self):
        print("🔋 Battery is charging...")

# --- Using the Child Class ---
tesla = ElectricCar()

tesla.start_engine()   # Inherited from Grandparent (Vehicle)
tesla.drive()          # Inherited from Parent (Car)
tesla.charge_battery()  # Its own method