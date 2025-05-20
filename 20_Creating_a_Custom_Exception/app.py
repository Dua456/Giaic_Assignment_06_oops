
# Custom exception class banayi gayi hai
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)  # Parent class (Exception) ka constructor call

# Function jo age check karega
def check_age(age):
    if age < 18:
        raise InvalidAgeError  # Agar age 18 se choti ho to custom error raise kare
    else:
        print("Access granted.")  # Agar age 18 ya us se zyada ho to access milega

# Example usage
try:
    # User se age input le rahe hain
    user_age = int(input("Enter your age: "))
    check_age(user_age)  # Function call kar rahe hain
except InvalidAgeError as e:
    # Agar age 18 se kam ho to ye error catch hoga
    print(f"InvalidAgeError: {e}")
except ValueError:
    # Agar user valid number na de (e.g. letters), to ye error show hoga
    print("Please enter a valid number.")
