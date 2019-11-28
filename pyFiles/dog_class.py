class Dog:
    # Class attribute
    species = "Canis familiaris"
    # Constructor
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    #instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # "Dunder method" because it begins and end with double underscores.
    def __str__(self):
        return f"{self.name} is {self.age} years old"


philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}") # Philo's coat is brown
print(philo.speak('uwu')) # Philo says uwu
print(philo.description()) # Philo is 5 years old