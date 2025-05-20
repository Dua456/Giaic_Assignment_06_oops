
class Car:
    def __init__(self, brand):
        # Public Variable
        self.brand = brand

    # Public Method
    def start(self):
        print(f"The {self.brand} has started.")


# Creating an object of Car
car1 = Car("Toyota")
print("Brands:", car1.brand)


# Calling public Method
car1.start()



