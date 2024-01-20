# Write an abstract class with name Employee
# Write 2 employee classes by inheriting from abstract Employee
# Write function
# get_info -> return string with name and position
# calculate_salary -> return float with information about employee salary
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self):
        return f"Name: {self.name}, position: {self.position}"

class Accountant(Employee):
    def __init__(self, name, position, bonus):
        super().__init__(name, position)
        self.bonus = bonus

    def calculate_salary(self):
        base_salary = 50000  
        return base_salary + self.bonus

class Developer(Employee):
    def __init__(self, name, position, bonus2):
        super().__init__(name, position)
        self.bonus2 = bonus2

    def calculate_salary(self):
        base_salary = 70000  
        return base_salary + self.bonus2


Accountant = Accountant("A.Sargsyan", "Accountant", 10000)
Developer = Developer("M.Sarsgsyan", "Developer", 800)

print(Accountant.get_info())
print(f"Salary: ${Accountant.calculate_salary()}")

print(Developer.get_info())
print(f"Salary: ${Developer.calculate_salary()}")


