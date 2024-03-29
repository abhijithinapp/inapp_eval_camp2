import os
from sys import flags
class Utils:
    def getInt():
        while(True):
            try:
                value = int(input())
                return value
            except:
                print("Enter a valid number")
                continue
    def getName():
        while(True):
            value = input()
            if ':' not in value:
                return value
            else:
                print("\':\' cannot be entered in name")
                continue

def initialiseContactsDB():
    if os.path.isdir('contacts'):
        pass
    else:
        os.mkdir("contacts")
    os.chdir("contacts")
    if os.path.exists("contacts.txt"):
        print("Opening Contact Database...")
        pass
    else:
        myFile = open("contacts.txt", "w")
        print("No existing database found! Creating new one..")
        myFile.close()

def searchByNumber(enteredNumber, isAddContact):
    if os.path.exists("contacts.txt"):
            myFile = open("contacts.txt", "r")
            contacts = myFile.readlines()
            myFile.close()
            flag = 0
            for contact in contacts:
                name,number = contact.strip().split(" : ")
                number= int(number)
                if number == enteredNumber:
                    print("Contact Already Exists" if isAddContact else "Contact Found")
                    print("" if isAddContact else f"""Name: {name} 
Phone number: {number}\n2""") 
                    flag = 1
                    return True
            if flag == 0:
                print("" if isAddContact else "No such Contact exists")
                return False
    else:
        print("Contacts database not found. Please wait for a while and check again.")

def addContact():
        print("Enter Name: ")
        name = Utils.getName()
        print("Enter Phone NUmber: ")
        number = Utils.getInt()
        if os.path.exists("contacts.txt"):
            if not searchByNumber(number, True):
                myFile = open("contacts.txt", "a")
                myFile.write(name.strip()+" : "+str(number)+"\n")
                print("Contact added.")
                myFile.close()
            else:
                print("Contact already exists")
        else:
            print("Contacts database not found. Please wait for a while and check again.")

def listAllContacts():
    if os.path.exists("contacts.txt"):
            myFile = open("contacts.txt", "r")
            contacts = myFile.readlines()
            myFile.close()
            contacts.sort()
            for contact in contacts:
                name,number = contact.strip().split(" : ")
                number = int(number)
                print(f"""Name: {name} 
Phone number: {number}\n""") 
    else:
        print("Contacts database not found. Please wait for a while and check again.")

def searchByName(enteredName):
    if os.path.exists("contacts.txt"):
            myFile = open("contacts.txt", "r")
            contacts = myFile.readlines()
            myFile.close()
            flag = 0
            for contact in contacts:
                name,number = contact.strip().split(" : ")
                number = int(number)
                if name == enteredName:
                    print("Contact Found")
                    print(f"""Name: {name} 
Phone number: {number}\n2""") 
                    flag = 1
            if flag == 0:
                print("No such Contact exists")
    else:
        print("Contacts database not found. Please wait for a while and check again.")

def deleteContact(enterednumber):
    if os.path.exists("contacts.txt"):
            myFile = open("contacts.txt", "r")
            contacts = myFile.readlines()
            myFile.close()
            flag = 0
            for contact in contacts:
                name,number = contact.strip().split(" : ")
                number = int(number)
                if number == enterednumber:
                    contacts.remove(contact)
                    print(f"Contact with name {name} Deleted")
                    flag = 1
            myFile = open("contacts.txt", "w")
            contacts = myFile.writelines(contacts)
            myFile.close()
            if flag == 0:
                print("No such Contact exists")
    else:
        print("Contacts database not found. Please wait for a while and check again.")

initialiseContactsDB()
while(True):
    print("""Enter your required option:
    1. Add Contact
    2. List Contact
    3. Search by Name
    4. Search by Number
    5. Delete a number
    6. exit
    """)
    option = Utils.getInt()
    match(option):
        case 1: addContact()
        case 2: listAllContacts()
        case 3: 
            print("Enter name:")
            name = Utils.getName()
            searchByName(name)
        case 4: 
            print("Enter Number: ")
            number = Utils.getInt()
            searchByNumber(number,False)
        case 5: 
            print("Enter Number: ")
            number = Utils.getInt()
            deleteContact(number)
        case 6: break
        case _: 
            print("Invalid option")
            continue
