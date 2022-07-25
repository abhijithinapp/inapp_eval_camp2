from abc import ABC, abstractmethod
class Utils:
    @staticmethod
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Invalid input')

    @staticmethod
    def getFloat(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Invalid input')

class Calculate(ABC):
    @abstractmethod
    def calculate(self):
        pass

    @property 
    def number1(self):
        return self.__number1

    @property 
    def number2(self):
        return self.__number2
    
    @number1.setter
    def number1(self, number1):
        if type(number1) == int or type(number1) == float:
            self.__number1 = number1
        else:
            print('Invalid Input')

    @number2.setter
    def number2(self, number2):
        if type(number2) == int or type(number2) == float:
            self.__number2 = number2
        else:
            print('Invalid Input1')


class CalcSum(Calculate):
    def calculate(self):
        return self.number1 + self.number2
    
class CalcDiff(Calculate):
    def calculate(self):
        return self.number1 - self.number2
class CalcProd(Calculate):
    def calculate(self):
        return self.number1 * self.number2

class CalcQuo(Calculate):
    def calculate(self):
        return self.number1/self.number2

    @Calculate.number2.setter
    def number2(self, number2):
        if number2 == 0:
            raise Exception
        else:
            Calculate.number2.fset(self, number2)


options = {
    1: ('Sum:', CalcSum),
    2: ('Difference:', CalcDiff),
    3: ('Product:', CalcProd),
    4: ('Quotient:', CalcQuo)
}


while(True):
    option = Utils.getInt('''Enter your choice
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    ''')
    if option not in range(1,6):
        print('Invalid input')
        continue
    if option == 5:
        break
    
    option, Class = options[option]
    obj = Class()
    obj.number1 = Utils.getFloat('Num1: ')
    while(True):
        try:
            obj.number2 = Utils.getFloat('Num2: ')
            break
        except:
            print("Cannot be zero")

    print(option, obj.calculate())
    



