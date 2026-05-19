class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):#instance method hai, kyunki isme self parameter hai
          print(f"laptop has {self.RAM} RAM and {self.storage}  {self.storage_type}") 

l1 = Laptop("16GB","1TB")   
l2 = Laptop("8GB","512GB")

l1.get_info()