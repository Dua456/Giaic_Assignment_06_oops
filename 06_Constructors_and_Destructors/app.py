
class Logger:
    # Constructor
    def __init__(self):
        print("Logger initialized. Object is created.")

    # Destructor
    def __del__(self):
        print("Logger destroyed. Object is deleted.")

# Calling the Constructor
log = Logger()

# Calling the destructor
del log

# print(log) Error

