# Logic:
# 1. Create Vehicle parent class
# 2. Create Car and Bike subclasses
# 3. Add extra attributes in subclasses
# 4. Create objects and display details

# Parent class
class Vehicle:

    # Constructor use kiya vehicle details store karne ke liye
    def __init__(self, brand, model):

        # Vehicle details store ki
        self.brand = brand
        self.model = model


# Car class
class Car(Vehicle):

    # Constructor
    def __init__(self, brand, model, seats):

        # Parent constructor call kiya
        super().__init__(brand, model)

        # Seats store ki
        self.seats = seats

    # Display method
    def display(self):

        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Seats =", self.seats)


# Bike class
class Bike(Vehicle):

    # Constructor
    def __init__(self, brand, model, engine_cc):

        # Parent constructor call kiya
        super().__init__(brand, model)# super() ka use karte hai jab hume parent class ke constructor ko call karna ho taki parent class ke attributes bhi initialize ho jaye

        # Engine cc store kiya
        self.engine_cc = engine_cc

    # Display method
    def display(self):

        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Engine =", self.engine_cc, "cc")


# Objects create kiye
c1 = Car("Toyota", "Fortuner", 6)
b1 = Bike("classic", "Royal Enfield", 390)

# Methods call kiye
c1.display()
b1.display()


# Q5: Create Vehicle class with Car and Bike subclasses and add extra attributes in subclasses