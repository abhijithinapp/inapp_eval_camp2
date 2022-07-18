import re
# name = '{} is my country. All Indians are my brothers and sisters.'.format('India')
# print(name)
# print(name.count('India'))

#regular expressions

#matching an email within a string using special sequence
myString = "my email is abhi@abhi.com hopw you will note it down"

#regular expression to match email
#check for non space chars before and after '@'
regex = '\S+@\S+'
x= re.findall(regex, myString)
print(x)

#append to add a value to the end of the list 
studentsAge = []
studentsAge.append(16)
studentsAge.append("hi")
print(studentsAge)

del studentsAge[-1]
print(studentsAge)

#combine two lists using extend()

studentsName = ['Anu', 'Binu', 'Sinu']
studentsAge.extend(studentsName)
print(studentsAge)

#to check if a variable is in the list
print('Anu' in studentsName)

#get the number of items in the list
print(len(studentsName))

#sort the list either alphabetically or  numerically
studentsAge.sort()
print(studentsAge)

#list concatenation using + operator
print(studentsName + studentsName)
print(studentsName)

#list duplication/multiplication using * operator
print(studentsName*3)
print(studentsName)

