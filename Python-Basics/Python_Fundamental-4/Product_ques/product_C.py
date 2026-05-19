class Product:

    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_price(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products: {cls.count}")

    @staticmethod
    def get_discounted_price(price, discount):
        print(f"Discounted price is Rs.{price - (price * discount / 100)}")


p1 = Product("Laptop", 40_000)
p1.get_discounted_price(p1.price, 12)