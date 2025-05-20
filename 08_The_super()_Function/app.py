
class Person:
    def __init__(self, name):
        self.name = name

# Inheret class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling parent constructor name
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Suncject: {self.subject}")

teacher = Teacher("Mubashir Ali", "Python")
teacher.display()