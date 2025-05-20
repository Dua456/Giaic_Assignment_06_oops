
# Countdown class banayi gayi hai
class Countdown:
    def __init__(self, start):
        self.current = start  # Countdown kis number se start hoga

    def __iter__(self):
        return self  # Ye object khud hi iterator ke tarah behave karega

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Jab number 0 se neeche ho jaye to loop stop ho jaye
        value = self.current  # Current value ko store kar rahe hain
        self.current -= 1     # Current value ko 1 se kam kar rahe hain
        return value          # Current value ko return kar rahe hain

# Example usage
countdown = Countdown(10)  # Countdown 10 se start hoga

print("Countdown:")
for number in countdown:  # For loop se Countdown class ko iterate kar rahe hain
    print(number)         # Har step pe ek number print hoga
