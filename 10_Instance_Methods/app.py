
class Dog:
    def __init__(self, name, breed):
        self.name = name        # Instace variable
        self.breed = breed      # Instance variable

    def bark(self):     # Instnce method
        print(f"{self.name} who is a {self.breed} says: Woof Woof!")

# Creating object of a Dog class
dog1 = Dog("Max", "German Shepherd")

# Calling the instance methods
dog1.bark()
