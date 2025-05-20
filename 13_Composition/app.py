
class Engine:
    def start(self):
        print("Engin started.")

# Class Car using Composition
class Car:
    def __init__(self, engine):
        self.engine = engine    # Composition: Can has an Engin.

    def start_car(self):
        print("Starting the engine...")
        self.engine.start()     # Access Engin's method

# Creating an onject for the engin
engine = Engine()

# Now passing the Engine onject to the class Car
car = Car(engine)

# Using Car to start the engine
car.start_car()