class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}") 

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (price*discount/100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16GB", "1TB")

l1.calc_discount(40_000,10)