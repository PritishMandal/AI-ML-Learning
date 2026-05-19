class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_price(self):
        print (f"Price of {self.name} is Rs.{self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total products: {cls.count}")

p1 = Product("Laptop", 40_000)
p2 = Product("Mobile", 20_000)
p3 = Product("Tablet", 15_000)


Product.get_count()