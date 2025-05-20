
# Base class A
class A:
    def show(self):
        print(f"Showing from class A")

# class B inherits from A
class B(A):
    def show(self):
        print(f"Showing from class B")

# class C inhertis from A
class C(A):
    def show(self):
        print(f"Showing from C")

# class D inherits from both B and C
class D(B,C):
    def show(self):
        pass

# Creating an object of class D
d = D()

# This will follow Method Resolution Order (MRO)
print(d.show())

