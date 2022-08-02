from random import randint
import re
from prettytable import PrettyTable

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
    def getName(*msg):
        while(True):
            value = input(*msg)
            if len(value) > 0:
                return value
            else:
                print("Product name should be minimum 1 character long")
                continue

MAX_PRODUCTS_IN_EACH_CATEGORY = Utils.getInt('Enter maximum value in each category: ')
products = dict()
class Category(): 
    def __init__(self, products = 0):
        self.__numberOfProductsPresent = products
    
    def incrementnumberOfProductsPresent(self):
        self.__numberOfProductsPresent = self.__numberOfProductsPresent +1
    
    @property
    def numberOfProductsPresent(self):
        return self.__numberOfProductsPresent

class Hygiene(Category):
    def __init__(self):
        super().__init__()
        self.__code = 'HY'
    @property 
    def code(self):
        return self.__code  
    
class Health(Category):
    def __init__(self):
        super().__init__()
        self.__code = 'HE'
    @property 
    def code(self):
        return self.__code  

class Staples(Category):
    def __init__(self):
        super().__init__()
        self.__code = 'ST'
    @property 
    def code(self):
        return self.__code  

class Sports(Category):
    def __init__(self):
        super().__init__()
        self.__code = 'SP'
    @property 
    def code(self):
        return self.__code  

class Fashion(Category):
    def __init__(self):
        super().__init__()
        self.__code = 'FA'
    @property 
    def code(self):
        return self.__code  
        
        
class validNameException(Exception):
    pass

class Product:
    @property
    def productName(self):
        return self.__productName

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
    def mrp(self):
        return self.__mrp

    @property 
    def discount(self):
        return self.__discount

    @productName.setter 
    def productName(self, name):
        if re.match('[a-zA-Z]{3,}$', name):
            self.__productName = name
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
    
    @mrp.setter
    def mrp(self,mrp):
        self.__mrp = mrp

    @discount.setter 
    def discount(self, discount):
        self.__discount = discount

    def increasemrpByPercent(self,percent):
        self.__mrp = round((100+percent)*self.__mrp/100,2)
         
categories = {
    1: Hygiene(),
    2: Health(),
    3: Staples(),
    4: Sports(),
    5: Fashion()
}

def addProducts():

    categoryoption = Utils.getCategory('''Enter the number corresponding to category:
        1. Hygiene
        2. Health
        3. Staples
        4. Sports
        5. Fashion
        ''')
    category = categories[categoryoption]
    if category.numberOfProductsPresent < MAX_PRODUCTS_IN_EACH_CATEGORY:
       
        product = Product() 
        while(True):
            try:
                name = Utils.getName("Enter name: ")
                product.productName = name
            except Exception as e:
                print (e)
            else: break

        #codeblock to generate product code
        productCodeWord = name[:2].upper()
        categoryCodeWord = category.code 
        coderegex = f'^{categoryCodeWord}{productCodeWord}'
        numberofProductsWithSameCodeWord = len(list(filter(lambda x: re.match(coderegex,x),list(products.keys()))))
        lastThreeRandomValues = '{0:03d}'.format(randint(0,999))
        productCode=f'{categoryCodeWord}{productCodeWord}{str(numberofProductsWithSameCodeWord)}{lastThreeRandomValues}'
        
        product = Product()
        taxPercent = Utils.getInt("Enter tax percent: ")
        product.taxPercent = taxPercent
        product.productCode = productCode

        while(True):
            priceOption = Utils.getInt('''
            Enter Price as:
            1. Including Tax
            2. Excluding tax''')

            price = Utils.getInt("Enter Price: ")
            match(priceOption):
                case 1: 
                    product.mrp = price
                    product.basicPrice = round(((100-product.taxPercent)*price)/100,2)
                    break
                case 2:
                    product.mrp = round(((100+product.taxPercent)*price)/100,2)
                    product.basicPrice = price
                    break
                case _:
                    print("Enter valid option")

        while(True):
            discountOption = Utils.getInt('''
            Enter Discount as:
            1. Percentage
            2. Absolute price''')

            discount = Utils.getInt("Enter Discount: ")
            match(discountOption):
                case 1: 
                    product.discount = discount
                    break
                case 2:
                    product.discount = round(((product.mrp)*discount)/100,2)
                    break
                case _:
                    print("Enter valid option")

        products.update({productCode: product})
        category.incrementnumberOfProductsPresent()
        print('Entered the product to database' )
    else:
        print('Cannot Enter the product as the maximum products in this category exceeded')

def listAllProducts():
    if (len(products))>0:
        myTable = PrettyTable(["Product Code" ,"tax%", "Base Price", "Tax Amount", "MRP", "Discout Percent", "Discount Amount", "Selling Price"])
        print(products.items())
        for productcode,product in products.items():
            # productName = product.productName
            taxPercent = product.taxPercent
            taxAmount = round((product.taxPercent*product.basicPrice)/100,2)
            basePrice = product.basicPrice
            mrp = product.mrp
            discountPercent = round((product.discount*product.basicPrice)/100,2)
            discountAmount = product.discount
            sellingPrice = product.mrp - product.discount
            myTable.add_row([productcode,taxPercent,basePrice,taxAmount, mrp, discountPercent, discountAmount,sellingPrice])
        print(myTable)
    else: 
        print("No products found")

def generateInvoice():
    xyzproduct = Product()
    xyzproduct.taxPercent = 18
    xyzproduct.mrp = 742
    #after increase of mrp by 18 %
    xyzproduct.increasemrpByPercent(18)
    #after increase of mrp by 10 %
    xyzproduct.increasemrpByPercent(10)
    print('Discout price: ', round(0.4*xyzproduct.mrp,2))
    #after 40 % discount
    xyzproduct.increasemrpByPercent(-40)
    print('Price Before tax: ',(100-xyzproduct.taxPercent) * xyzproduct.mrp/100)
    print('mrp: ',xyzproduct.mrp)

while(True):
    print("""Enter your required option:
    1. Add Products
    2. List All Products
    3. Generate Invoice
    4. Exit
""")
    option = Utils.getInt()
    match(option):
        case 1: addProducts()
        case 2: listAllProducts()
        case 3: generateInvoice()
        case 4: exit()
        case _: print("Invalid option")