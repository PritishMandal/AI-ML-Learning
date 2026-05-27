class Student:
    college = "TGPCET college"
    
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Pritish",9.4)

print(stu1.name)
print(Student.college)