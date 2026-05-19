class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


        

stu1 = Student("Shrutika", 9.5)
stu2 = Student("Pritish", 9.0)
stu3 = Student("Rohith", 9.2)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")