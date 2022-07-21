from unicodedata import name


class Calculator:
    input1 = 0
    input2 = 0

    def __init__(self,input1, input2):
        Calculator.input1 = input1
        Calculator.input2 = input2

    def add(self):
        print("Sum is: ",Calculator.input1 + Calculator.input2)

    def multiply(self):
        print("Product is: ",Calculator.input1 * Calculator.input2)               
        
    def divide(self):
        if Calculator.input2 == 0 :
            print("Division not possible due to division by zero error")
        else: 
            print("Qoutient is: ",Calculator.input1 / Calculator.input2)               

calculation1 = Calculator(1,0)
calculation1.add()
calculation1.multiply()
calculation1.divide()