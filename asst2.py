import re
numberList = [1, 2, 6, 4, 9, 6, 22]

# 1. sort in asdcending order and print the first element in the list
numberList.sort()
print(numberList[0])

# 2. sort the second largest number in the list
print(numberList[-2])

# 3. to print odd and even nnumbers seperately
numbersList = [i for i in range(11)]
oddNumbers = numbersList[1:11:2]
evenNumbers = numbersList[2:11:2]

print(evenNumbers, oddNumbers)

# 4. program to reverse  a list
numberList.reverse()
print(numberList)

# 5. Program to print all odd numbers from 1-50
print([x for x in range(1, 50, 2)])

# 6. prgogram to count Even and Odd numbers in a list
countEven = 0
countOdd = 0
for x in numberList:
    if x % 2 == 0:
        countEven = countEven+1
    else:
        countOdd = countOdd + 1
print("Number of Even numbers is {0} and Number of Odd numbers is {1}".format(
    countEven, countEven))

# regexp

# 1. remove zeroes from an ip address
IP_ADDRESS = "216.08.094.196"
print(IP_ADDRESS.replace('0', ''))

# 2. match a string that has an a followed by anything ending in b
text = "Hi this is arnab"
print(re.findall(r"\s\w*[Aa].*b$", text))

# 3. Replace 6 with six and 10 with ten
text = 'They ate 6 apples and 10 bananas'
text = text.replace('6', 'six')
text = text.replace('10', 'ten')
print(text)
