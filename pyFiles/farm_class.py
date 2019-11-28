# Parent class
class Animal:
    def __init__(self, legs, produce, sex):
        self.legs = legs
        self.produce = produce
        self.sex = sex

    def __str__(self, extra=""):
        return f"{self.legs} legs, produces {self.produce}, sex is {self.sex}{extra}"

# Inherients from Animal
class Cow(Animal):
    def __init__(self, legs, produce, sex, horns):
        # super() indicates that it uses the parent class __init__
        super().__init__(legs, produce, sex)
        self.horns = horns

    def __str__(self, extra=''):
        return super().__str__(extra=f" and has {self.horns} horns.")

    def milked(self):
        print("ew")

class Chicken(Animal):
    def __init__(self, legs, produce, sex, eggs):
        super().__init__(legs, produce, sex)
        self.eggs = eggs
    
    def yougetthepoint(self):
        return 420

class Pig(Animal):
    def __init__(self, legs, produce, sex, smell):
        super().__init__(legs, produce, sex)
        self.smell = smell

berta = Cow(4, "milk", "f", 2)
print(berta) # 4 legs, produces milk, sex is f and has 2 horns.
brunhilde = Animal(1, "null", "x")
print(brunhilde) # 1 legs, produces null, sex is x
berta.milked() # ew
