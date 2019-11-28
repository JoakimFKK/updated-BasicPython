class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says '{sound}'"

class JackRussellTerrier(Dog):
    # sound="arf" means default value is "arf" if not stated.
    def speak(self, sound="Arf"):
        # super() python searches the parent class for a .speak() method and calls it with the variable "Sound"
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
oddie = GoldenRetriever("Oddie", 15)


print(oddie.speak()) # Oddie says 'Bark'
