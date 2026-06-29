# Logic:
# 1. Create Person class
# 2. Use default parameters in constructor
# 3. Allow multiple ways to create object
# 4. Display object details

class Person:

    # Constructor
    def __init__(self, name, age=None, address=None):#ye default parameters use karta hai, jisse hum multiple ways se object create kar sakte hain

        # Details store ki
        self.name = name
        self.age = age
        self.address = address

    def display(self):

        print("Name =", self.name)
        print("Age =", self.age)
        print("Address =", self.address)



p1 = Person("Pitu")

p2 = Person("shanku", 21)

p3 = Person("annu", 21, "Bhopal")

# Methods call kiye
p1.display()
p2.display()
p3.display()


# Q7: Create Person class using default parameters to simulate constructor overloading