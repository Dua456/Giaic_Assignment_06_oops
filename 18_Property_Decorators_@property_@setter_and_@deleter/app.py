
class Product:
    def __init__(self, price):
        # Jab object banega to price set hoga (setter call hoga)
        self.price = price

    # Getter method – jab price read karein to ye chalega
    @property
    def price(self):
        print("Getting the price...")
        return self._price  # Note: _price use karte hain andar

    # Setter method – jab price set karein to ye chalega
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")  # Agar price negative ho to error message
        else:
            print("Setting the price...")       # Warna price set ho jayega
            self._price = value                 # _price me value store kar rahe hain

    # Deleter method – jab price delete karein to ye chalega
    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price  # _price attribute delete kar diya jaega

# Object create kiya Product class ka
item = Product(1000)        # price set hoga (setter chalega)
print(item.price)          # price access kiya (getter chalega)
item.price = 1500           # price update kiya (setter chalega)
print(item.price)          # dobara access kiya (getter chalega)
del item.price             # price delete kiya (deleter chalega)
