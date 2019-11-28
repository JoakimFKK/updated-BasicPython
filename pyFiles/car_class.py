class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    # When a Car object is turned to a string, it returns this.
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

    def drive(self, distance):
        self.mileage += distance

blue = Car("blue", 20000)
red = Car("red", 30000)

print(blue) # The blue car has 20000 miles
print(red) # The red car has 30000 miles

blue.drive(100)
red.drive(500)

print(blue) # The blue car has 20100 miles
print(red) # The red car has 30500 miles