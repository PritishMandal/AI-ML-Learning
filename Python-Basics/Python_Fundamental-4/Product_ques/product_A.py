class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        print (f"Price of {self.name} is {self.price}")

p1 = Product("Laptop", 40_000)
p2 = Product("Mobile", 20_000)
p3 = Product("Tablet", 15_000)

p1.get_price()