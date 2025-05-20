
# Multiplier class banayi gayi hai
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # factor ko object ke andar store kar rahe hain

    # __call__ method object ko function ki tarah banata hai
    def __call__(self, number):
        return self.factor * number  # number ko factor se multiply karke return karta hai

# Multiplier class ka object banaya jisme factor = 5
multiplier = Multiplier(5)

# Check kar rahe hain kya object callable hai (function ki tarah use ho sakta hai)
print(callable(multiplier))  # Output: True

# Object ko function ki tarah call kar rahe hain
result = multiplier(10)  # Actually calls multiplier.__call__(10)
print(result)  # Output: 50
