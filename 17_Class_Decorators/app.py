# Yaha decorator ek nayi method class mein add karega
def add_greetings(cls):
    # Ek nayi method define kiya gaya hai
    def greet(self):
        return "Hello from Decorator!"  # Jab call hogi to ye message show hoga

    cls.greet = greet  # greet method ko class mein add kar diya
    return cls  # Updated class return kar rahe hain

# Person class par decorator lagaya gaya hai
@add_greetings
class Person:
    def __init__(self, name):
        self.name = name  # Naam ko object ke saath store kar rahe hain

# Object create kar rahe hain
p1 = Person("Dua Shakir")

# Object ka name print kar rahe hain
print(p1.name)

# greet method (jo decorator se aayi hai) call kar rahe hain
print(p1.greet())
