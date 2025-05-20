
class Bank:
    # Class variable
   bank_name = "HBL"

   @classmethod
   def change_bank_name (cls,name):
      cls.bank_name = name


b1 = Bank()
print(b1.bank_name)

# Changing bank name using class method
Bank.change_bank_name("Meezan Bank")

print(b1.bank_name)

