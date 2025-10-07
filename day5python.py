class Car:
    def __init__(self, brand):
        self.brand = "tata"


c = Car("tata")
print(c.brand)  



class Bank:
    def __init__(self):
        self.balance = 1000  

    def get_balance(self):
        return self.balance


b = Bank()
print(b.get_balance())
