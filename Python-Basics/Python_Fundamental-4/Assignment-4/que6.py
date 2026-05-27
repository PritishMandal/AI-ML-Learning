# Logic:
# 1. Create abstract Employee class
# 2. Create abstract method calculate_salary()
# 3. Create subclasses and override method
# 4. Create objects and call methods

# ABC module import kiya
from abc import ABC, abstractmethod


# Abstract class
class Employee(ABC):

    # Abstract method
    @abstractmethod
    def calculate_salary(self):
        pass


# Intern class
class Intern(Employee):

    # Salary method
    def calculate_salary(self):

        print("Intern Salary = 5000")


# FullTimeEmployee class
class FullTimeEmployee(Employee):

    # Salary method 
    def calculate_salary(self):

        print("Full Time Employee Salary = 50000")


# ContractEmployee class tab use karte hai jab hume kisi employee ko contract basis pe rakhna ho jisme unka salary fixed hota hai aur unhe company ke benefits nahi milte
class ContractEmployee(Employee):

    # Salary method
    def calculate_salary(self):

        print("Contract Employee Salary = 30000")


# Objects create kiye
i = Intern()
f = FullTimeEmployee()
c = ContractEmployee()

# Methods call kiye
i.calculate_salary()
f.calculate_salary()
c.calculate_salary()


# Q6: Create abstract Employee class with calculate_salary() method and implement it differently in subclasses