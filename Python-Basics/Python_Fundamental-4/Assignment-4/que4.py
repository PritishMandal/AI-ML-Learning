# Logic:
# 1. Create Shape parent class
# 2. Create subclasses Circle, Rectangle and Triangle
# 3. Override area() method
# 4. Create objects and call methods

# Parent class
class Shape:

    # Area method
    def area(self):
        print("Area calculation")


# Circle class
class Circle(Shape):

    # Overridden method
    def area(self):

        radius = 5

        print("Circle Area =", 3.14 * radius * radius)


# Rectangle class
class Rectangle(Shape):

    # Overridden method
    def area(self):

        length = 10
        breadth = 5

        print("Rectangle Area =", length * breadth)


# Triangle class
class Triangle(Shape):

    # Overridden method
    def area(self):

        base = 8
        height = 4

        print("Triangle Area =", 0.5 * base * height)


# Objects create kiye
c = Circle()
r = Rectangle()
t = Triangle()

# Methods call kiye
c.area()
r.area()
t.area()


# Q4: Create Shape class with area() method and override it in Circle, Rectangle and Triangle classes