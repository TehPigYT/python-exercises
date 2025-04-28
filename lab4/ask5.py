import math

class Cylinder:
    def __init__(self, height, radius):
        self._height = height
        self._radius = radius

    def volume(self):
        return math.pi * (self._radius ** 2) * self._height

    def __str__(self):
        return f"Radius: {self._radius} | Height: {self._height} | Volume: {Cylinder.volume(self)}"

if __name__ == "__main__":
    valid_entries = 0
    cylinders = []
    while(valid_entries < 5):
        height = int(input(f"{valid_entries+1} | Enter height: "))
        if height < 0:
            print("Height not a valid number, also cannot be negative")
            continue

        radius = int(input(f"{valid_entries+1} | Enter radius: "))
        if radius < 0:
            print("Radius not a valid number, also cannot be negative")
            continue

        cylinder = Cylinder(height, radius)
        cylinders.append(cylinder)
        valid_entries += 1

    for cylinder in sorted(cylinders, key=lambda c: c.volume()):
        print(cylinder.__str__())
