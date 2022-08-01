"""
Q3. The denominations in Indian currency are:
|1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
Given an amount N, print how many coins/notes make up N
Sample input:
Enter the amount: 2640
Output:
2000 1
500 1
100 1
10 4
Also test your program with N=3781, 4928, and 5134
"""


from this import d


class Utils:
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print("Enter a valid number")
                continue

class Currencies:
    def __init__(self):
        self.__one = None
        self.__two = None
        self.__two = None
        self.__five = None
        self.__ten = None
        self.__twenty = None
        self.__fifty = None
        self.__hundred = None
        self.__twoHundred = None 
        self.__fiveHundred = None
        self.__twoThousand = None

    def findDenominations(self,amount):
        remainingamount = amount
        while(remainingamount>0):
            if remainingamount>=2000:
                self.__twoThousand = amount//2000
                remainingamount = remainingamount%2000
            elif remainingamount>=500:
                self.__fiveHundred = remainingamount//500
                remainingamount = remainingamount%500
            elif remainingamount>=200:
                self.__twoHundred = remainingamount//200
                remainingamount = remainingamount%200
            elif remainingamount>=100:
                self.__hundred = remainingamount//100
                remainingamount = remainingamount%100
            elif remainingamount>=50:
                self.__fiveHundred = remainingamount//50
                remainingamount = remainingamount%50
            elif remainingamount>=20:
                self.__twenty = remainingamount//20
                remainingamount = remainingamount%20
            elif remainingamount>=10:
                self.__ten = remainingamount//10
                remainingamount = remainingamount%10
            elif remainingamount>=5:
                self.__five = remainingamount//5
                remainingamount = remainingamount%5
            elif remainingamount>=2:
                self.__two = remainingamount//2
                remainingamount = remainingamount%2
            elif remainingamount>=1:
                self.__one = remainingamount//1
                remainingamount = remainingamount%1
            else:
                print("Done!!")
                
    def displaydenominations(self):
        if self.__twoThousand:
            print(f"2000: {self.__twoThousand}")
        if self.__fiveHundred:
            print(f"500: {self.__fiveHundred}")
        if self.__twoHundred:
            print(f"200: {self.__twoHundred}")
        if self.__hundred:
            print(f"100: {self.__hundred}")
        if self.__fifty:
            print(f"50: {self.__fifty}")
        if self.__twenty:
            print(f"20: {self.__twenty}")
        if self.__ten:
            print(f"10: {self.__ten}")
        if self.__five:
            print(f"5: {self.__five}")  
        if self.__two:
            print(f"2: {self.__two}")      
        if self.__one:
            print(f"1: {self.__one}")

while(True):
    amount = Utils.getInt('Enter Amount: ')
    notes = Currencies()
    notes.findDenominations(amount)
    notes.displaydenominations()
    while(True):
        option = input("Do you want to find more denominations?(y/n)").lower()
        match(option):
            case 'y': break
            case 'n': exit()
            case '_': continue
                
                