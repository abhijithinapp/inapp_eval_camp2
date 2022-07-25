phoneNumbers = {}

def addContact():
    name = input("Enter name: ")
    phoneNumber = input("Enter Phone Number: ")
    phoneNumbers[name] = phoneNumber 
    print("Contact added")

def listAllContacts():
    for i,x in enumerate(phoneNumbers):
        print("{}. Name: {} Phonenumber: {}".format(i+1,x,phoneNumbers[x]))
    
def deleteContact():
    for x in phoneNumbers:
        print("Name: {}    Phonenumber: {} ".format(x,phoneNumbers[x]))
    nameToBeDeleted = input("Enter the name to be deleted: ")
    if nameToBeDeleted in phoneNumbers.keys():
        del phoneNumbers[nameToBeDeleted]
        print("Number Deleted!")
    else: 
        print("Name not found")
def searchByName():
    name = input("Enter the name to be searched: ")
    if name in phoneNumbers.keys():
        print("Name: {}     Phone Number: {}".format(name,phoneNumbers[name]))
    else:
        print("Name not found")

def searchbyNumber():
    phn = input("Enter the phone number: ")
    if phn in phoneNumbers.values():
        for name,phn_number in phoneNumbers.items():
            if phn_number == phn:
                print("Name : {} Phone Number: {}".format(name,phn_number))
    else:
        print("Phone number not found") 

def actionToSelectedOption(option):
    match(option):
        case 1: listAllContacts()
        case 2: addContact()
        case 3: deleteContact()
        case 4: searchByName()
        case 5: searchbyNumber()
        case 6: exit()
        case _: print("Wrong choice")
            

while(1):
    option = int(input("""
Choose the required option
1. List all contacts
2. Add a new contact
3. Delete a contact
4. Search by name
5. Search by number
6. exit
 
"""))
    actionToSelectedOption(option)
    
