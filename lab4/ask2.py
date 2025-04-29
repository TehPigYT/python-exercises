class Juice:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price

    def __str__(self):
        return self.name + " (" + str(self.capacity) + "L)"

    def __add__(self, other):
        new_price = self.price + other.price
        return Juice(
            self.name + "&" + other.name, self.capacity + other.capacity, new_price
        )

    def pour(self, percentage):
        assert 0.0 < percentage <= 1.0
        print(f"Pour {percentage*100}% from {str(self)}")
        new_capacity = self.capacity * percentage
        new_price = self.price * percentage
        self.capacity -= new_capacity
        self.price -= new_price
        return Juice(self.name, new_capacity, new_price)


a = Juice("Orange", 1.5, 40)
b = Juice("Apple", 2.0, 70)

result = a + b
print(result)

c = result.pour(0.7)
print(result)
print(c)
