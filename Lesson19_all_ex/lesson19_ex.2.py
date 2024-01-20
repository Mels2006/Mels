# 2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division
class BasicCalculator:
    def addition(self,num_1,num_2):
        return num_1 + num_2
    def subtraction(self,num_3,num_4):
        return num_3 - num_4
    def multiplication(self,num_5,num_6):
        return num_5 * num_6
    def division(self,num_7,num_8):
        if num_8 != 0:
            return num_7 / num_8
        else:
            raise ZeroDivisionError("num_8 can't be 0")

calculator = BasicCalculator()

result_of_addition = calculator.addition(6,4)
result_of_subtraction = calculator.subtraction(7,5)
result_of_multiplication = calculator.multiplication(2,5)
result_of_division = calculator.division(49,7)

print(f"Addition: {result_of_addition}")
print(f"Subtraction: {result_of_subtraction}")
print(f"Multiplication: {result_of_multiplication}")
print(f"Division: {result_of_division}")