class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"Driving Vehicle by {self.make}, model {self.model}, manufactured in year {self.year}.")

class Car(Vehicle):
    def drive(self):
        print(f"Driving Car by {self.make}, model {self.model}, manufactured in year {self.year}.")

class Truck(Vehicle):
    def drive(self):
        print(f"Driving Truck by {self.make}, model {self.model}, manufactured in year {self.year}.")

vehicle = Vehicle("UwU", "Super", "2024")
car = Car("BMW", "MW350", "2005")
truck = Truck("truk", "u39", "1948")

vehicle.drive()
car.drive()
truck.drive()