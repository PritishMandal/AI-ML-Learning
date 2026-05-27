# Logic:
# 1. Create Student class
# 2. Use private attributes
# 3. Create getter and setter methods
# 4. Apply validation on data

class Student:

    # Constructor
    def __init__(self, name, roll_no, marks):

        # Setter methods call kiye
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Name setter method
    def set_name(self, name):

        # Empty name check kiya
        if name != "":
            self._name = name

        else:
            print("Name cannot be empty")

    # Roll number setter method
    def set_roll_no(self, roll_no):

        # Roll number range check ki
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no

        else:
            print("Invalid Roll Number")

    # Marks setter method
    def set_marks(self, marks):

        # Negative marks check kiye
        if marks >= 0:
            self._marks = marks

        else:
            print("Marks cannot be negative")

    # Getter methods 
    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks


# Object create kiya
s1 = Student("shruti frutii", 12, 29)

# Values print ki
print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())


# Q3:
# Create a class Student with private attributes
# _name, _roll_no and _marks
# Add getter and setter methods with validation