class Vehicle:
    def __init__ (self, model,year,brand):
        self.model = model
        self.year = year
        self.brand = brand
    def start_engine(self):
        print("The engine of the vehicle is starting.") 

class Car(Vehicle): 
    def __init__ (self,model,year,brand,transmission):
        super().__init__(model,year,brand)
        self.transmission = transmission
    def start_engine(self):
        print("My car is a " + self.year + " " + self.brand + " " + self.model + " with " + self.transmission + " transmission. The engine is starting now!")

myCar = Car("Corolla", "1997", "Toyota", "Manual")
myCar.start_engine()