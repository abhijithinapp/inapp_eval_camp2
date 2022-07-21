from unicodedata import name


class Calculator:
    input1 = 0
    input2 = 0

    def __init__(self,input1, input2):
        Calculator.input1 = input1
        Calculator.input2 = input2

    def add(self):
        print("Sum of",Calculator.input1,"and", Calculator.input2, "is", Calculator.input1 + Calculator.input2)

    def multiply(self):
        print("Product of", Calculator.input1,"and", Calculator.input2, "is",Calculator.input1 * Calculator.input2)               
        
    def divide(self):
        if Calculator.input2 == 0 :
            print("Division not possible due to division by zero error")
        else: 
            print("Qoutient of", Calculator.input1,"and", Calculator.input2, "is",Calculator.input1 / Calculator.input2)               

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
calculation1 = Calculator(num1,num2)
calculation1.add()
calculation1.multiply()
calculation1.divide()