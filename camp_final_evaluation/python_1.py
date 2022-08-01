from msilib.schema import Property
import numbers
from random import randint
import re
from abc import ABC, abstractmethod
from tkinter.font import names

class Utils:
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print("Enter a valid number")
                continue
    def getCategory(*msg):
        while(True):
            value = Utils.getInt(*msg)
            if value in range (1,6):
                return value
            else:
                print("Enter a valid number in range 0-6")
                continue

MAX_PRODUCTS_IN_EACH_CATEGORY = Utils.getInt('Enter maximum value in each category')
products = dict()
class Category(ABC): 
    def __init__(self, products = 0):
        self.__numberOfProductsPresent = products
    def incrementnumberOfProductsPresent(self):
        self.__numberOfProductsPresent = self.numberOfProductsPresent +1
    
    @property
    def numberOfProductsPresent(self):
        return self.__numberOfProductsPresent

class Hygiene(Category):
    def __init__(self):
        self.__code = 'HY'
    @property 
    def code(self):
        return self.__code  
    
class Health(Category):
    def __init__(self):
        self.__code = 'HE'
    @property 
    def code(self):
        return self.__code  

class Staples(Category):
    def __init__(self):
        self.__code = 'ST'
    @property 
    def code(self):
        return self.__code  

class Sports(Category):
    def __init__(self):
        self.__code = 'SP'
    @property 
    def code(self):
        return self.__code  

class Fashion(Category):
    def __init__(self):
        self.__code = 'FA'
    @property 
    def code(self):
        return self.__code  
        
        
class validNameException(Exception):
    pass

class Product:
    @property
    def name(self):
        return self.__name

    @property 
    def category(self):
        return self.__category

    @property 
    def productCode(self):
        return self.__productCode

    @property 
    def basicPrice(self):
        return self.__basicPrice

    @property 
    def taxPercent(self):
        return self.__taxPercent

    @property 
    def discount(self):
        return self.__discount

    @name.setter 
    def name(self, name):
        if re.match('[a-zA-Z]{3,}', name):
            self.__name = name
        else:
            raise validNameException('Name should be of atleast 3 letters and all characters')


    @category.setter 
    def category(self, category):
        self.__category = category

    @productCode.setter 
    def productCode(self, productCode):
        self.__productCode = productCode


    @basicPrice.setter 
    def basicPrice(self, basicPrice):
        self.__basicPrice = basicPrice
    
    @taxPercent.setter 
    def taxPercent(self, taxPercent):
        self.__taxPercent = taxPercent
    
    @discount.setter 
    def discount(self, discount):
        self.__discount = discount
    
    @name.setter 
    def name(self, name):
        if re.match('[a-zA-Z]{3,}', name):
            self.__name = name
        else:
            raise validNameException('Name should be of atleast 3 letters and all characters')

categories = {
    1: Hygiene(),
    2: Health(),
    3: Staples(),
    4: Sports(),
    5: Fashion()
}

def addProducts():
    name = input("Enter name")
    categoryoption = Utils.getCategory('''Enter the number corresponding to category:
        1. Hygiene
        2. Health
        3. Staples
        4. Sports
        5. Fashion''')
    category = categories[categoryoption]
    productCode = name[:2].upper()
    categoryCode = category.code 
    coderegex = '{categoryCode}{productCode}'
    numberofCodes = len([s for s in list(products.keys()) if re.match(coderegex,s)])
    lastThreeRandomValues = '{0:03d}'.format(randint(0,999))
    code=f'{categoryCode}{productCode}{str(numberofCodes)}{lastThreeRandomValues}'
    basicpice = Utils.getInt("enter price")
    product = Product()
    product.basicPrice=basicpice
    product.productCode = code
    products.update({code: product})
    print(list(products.keys()))
    




while(True):
    print("""Enter your required option:
    1. Add Products
    2. List All Products
    3. Exit
""")
    option = Utils.getInt()
    match(option):
        case 1: addProducts()
            

        case _: print("Invalid option")
            
