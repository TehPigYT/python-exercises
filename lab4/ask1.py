class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand} | Model: {self.model} | Year: {self.year}"


cars = """
#year,brand,model
1969,Dodge,Charger
1963,Corvette, Stingray
1974,Porsche,914
1969,Chevrolet,Camaro Z28
1967,Toyota,2000GT
1971,Ford,Thunderbird
1991,Dodge,Viper
1966,Lamborghini,Miura
1962,Ferrari,250 GTO
1954,Mercedes,300SL Gullwing
"""

car_list = []
for line in cars.split("\n"):
    line = line.strip()
    if line == "" or line[0] == "#":
        continue
    year, brand, model = line.split(",")
    car = Car(brand, model, int(year))
    car_list.append(car)

cars_list = sorted(car_list, key=lambda car: car.brand)
cars_list = sorted(car_list, key=lambda car: car.year)

for car in car_list:
    print(car)
