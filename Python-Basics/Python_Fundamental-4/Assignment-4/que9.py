# Logic:
# 1. Create Herbivore and Carnivore classes
# 2. Create Omnivore class using multiple inheritance
# 3. Create Bear class
# 4. Call methods from parent classes

# Herbivore class
class Herbivore:

    # Method
    def eat_plants(self):

        print("Bear eats plants")


# Carnivore class
class Carnivore:

    # Method
    def eat_meat(self):

        print("Bear eats meat")


# Omnivore class
class Omnivore(Herbivore, Carnivore):

    # Method
    def eat_all(self):

        print("Bear eats both plants and meat")


# Bear class
class Bear(Omnivore):

    # Display method
    def display(self):

        print("Bear is an Omnivore")


# Object create kiya 
b = Bear()

# Methods call kiye
b.display()
b.eat_plants()
b.eat_meat()
b.eat_all()


# Q9: Create Herbivore, Carnivore and Omnivore classes and demonstrate multiple inheritance using Bear class