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


l1 = Laptop("16GB", "1TB")

l1.get_storage_type()
l1.get_info()
