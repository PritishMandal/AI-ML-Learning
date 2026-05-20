class Employee:
    def get_details(self):
        print(" designnation = Employee")


class Teacher(Employee):
    def get_designation(self):
        print(" designnation = Teacher") # ye method Employee class ke method ko override kar raha hai

t1 = Teacher()
t1.get_designation()       