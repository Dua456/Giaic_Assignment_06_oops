
class Employee:
    def __init__(self, name , salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected
        self.__ssn = ssn        # Private
        
    def display(self):
        print(f"Name (Public): {self.name}")
        print(f"Salary (Protected): {self._salary}")
        print(f"SSN (Private): {self.__ssn}")

emp = Employee("Dua Shakir Hussain", 45000, "123-456-789")

# Accessing Public
print("Public name:", emp.name)

# Accessing Protected (allowed, but not recommended directly)
print("Protected Salary:", emp._salary)

# Accessing private variable using name (not recommended but possible)
print("Accessing Private SSN via name :", emp._Employee__ssn)