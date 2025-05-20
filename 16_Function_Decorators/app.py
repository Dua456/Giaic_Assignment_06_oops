
# Decorator function banaya gaya hai
def log_function_call(func):
    # Wrapper function jo original function se pehle message print karega
    def wrapper():
        print("function is being called")  # Function call se pehle ye print hoga
        return func()  # Original function ko call karega
    return wrapper  # Wrapper ko return karega

# say_hello function par decorator lagaya gaya hai
@log_function_call
def say_hello():
    print("Hello, World")  # Ye function ka asal kaam hai

# Function ko call kar rahe hain
say_hello()

