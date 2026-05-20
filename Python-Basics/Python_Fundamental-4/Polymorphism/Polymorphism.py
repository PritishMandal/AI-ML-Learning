class Employee:
    def get_details(self):
        print(" designnation = Employee")


class Teacher(Employee):
    def get_designation(self):
        print(" designnation = Teacher") 

t1 = Teacher()
t1.get_designation()       