"""
Q4. The following is called Floyd’s triangle:
1
2 3
4 5 6
7 8 9 10
11
· · ·
12 13 14 15
Given a positive integer N, write a program that prints N rows of Floyd’s
triangle, with the rows properly aligned
"""
from threading import currentThread


class Utils:
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print("Enter a valid number")
                continue
    

noOfROws = Utils.getInt('Enter number of rows in floyd\'s triangle ')
currentValue = 1
for i in range(1,noOfROws+1):
    for j in range(i):
        print(currentValue, end = " ")
        currentValue = currentValue + 1
    print() 