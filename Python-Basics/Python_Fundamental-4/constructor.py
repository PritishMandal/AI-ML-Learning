class Student:
    def __init__(self, name,cgpa):
      self.name = name
      self.cgpa = cgpa
        

stu1 = Student("Shrutika", 9.5)
stu2 = Student("Pritish", 9.0)
stu3 = Student("Rohith", 9.2)

print(stu1.name)
print(stu2.name)         
print(stu3.name)

print(stu1.cgpa)
print(stu2.cgpa)
print(stu3.cgpa)