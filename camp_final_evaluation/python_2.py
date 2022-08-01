
from ast import Break
import pyodbc
from prettytable import PrettyTable
import functools
CONN_STRING = 'Driver={SQL Server};Server=CPU1213\SQLEXPRESS;Database=camp2;Trusted_Connection=yes;'
MAX_LENGTH_OF_NAME_ALLOWED_IN_DB = 50
class Utils:
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print("Enter a valid number")
                continue
    
    def getAge():
        while (True):
            value = Utils.getInt("Enter age: ")
            if value > 0:
                return value
            else:
                print('Enter a valid age')
                continue

    def getName(*msg):
        while(True):
            value = input(*msg)
            if len(value) <= MAX_LENGTH_OF_NAME_ALLOWED_IN_DB:
                return value
            else:
                print("Maximum characters allowed is 50")
                continue
    
    def getGender():
        genders = getGenders()
        print("Enter number corresponding to your gender")
        for id, gender in genders.items():
            print(id,'. ', gender)   
        while(True):
            option =  Utils.getInt()
            if option in range(1,4):
                return option
            else:
                print("Enter a value in range 1-3")
                continue

    
    def getBloodGroup():
        bloodGroups = getBloodGroups()
        print("Enter number corresponding to your blood group:")
        for id, bloodGroup in bloodGroups.items():
            print(id,'. ', bloodGroup)   
        while(True):
            option =  Utils.getInt()
            if option in range(1,9):
                return option
            else:
                print("Enter a value in range 1-8")
                continue

def dbConnect(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            myconn = pyodbc.connect(CONN_STRING)
            cursor = myconn.cursor()
            result = myFunc(cursor,*args)
            myconn.commit()
            myconn.close()
            return result
        except Exception as e:
            print('Connection error')
            print(e)
    return innerWrapper

def getPatientDetailsFromUser():
    name = Utils.getName("Enter Patient Name: ")
    name = name.title()
    gender = Utils.getGender()
    age = Utils.getAge()
    bloodGroup = Utils.getBloodGroup()
    return name,gender,age,bloodGroup

@dbConnect
def getGenders(cursor):
    cursor.execute('SELECT * FROM gender')
    values = cursor.fetchall()
    genders = {row[0]: row[1] for row in values}
    return genders

@dbConnect
def getBloodGroups(cursor):
    cursor.execute('SELECT * FROM bloodGroup')
    values = cursor.fetchall()
    bloodGroups = {row[0]: row[1] for row in values}
    return bloodGroups

@dbConnect
def addPatient(cursor):
    name,gender,age,bloodGroup = getPatientDetailsFromUser()
    try: 
        cursor.execute('INSERT INTO patient(patientName, genderID, age, bloodGroupId) VALUES(?,?,?,?)',(name,gender,age,bloodGroup))
    except Exception as e:
        print('Something went wrong')
        print (e)
    else: 
        print('Patient added successfully')

@dbConnect
def updatePatient(cursor):
    listAllPatients()
    id = Utils.getInt("Enter the id of patient to be updated: ")
    try: 
        cursor.execute('SELECT * FROM patient WHERE patientId = ?',(id))
        if len(cursor.fetchall()) > 0:
            while(True):
                option = Utils.getInt('''
                Enter field to be updated
                1. Name
                2. Gender
                3. Age
                4. BloodGroup
                5. Cancel Update''')
                match(option):
                    case 1:
                        try:
                            name = Utils.getName('Enter new name')
                            cursor.execute('UPDATE patient SET patientName = ? WHERE patientId = ?',(name,id))
                        except: 
                            print('Something went wrong')
                        else:
                            print('Name updated successfully')
                    case 2:
                        try:
                            gender = Utils.getGender()
                            cursor.execute('UPDATE patient SET genderID = ? WHERE patientId = ?',(gender,id))
                        except: 
                            print('Something went wrong')
                        else:
                            print('Gender updated successfully')
                    case 3:
                        try:
                            age = Utils.getAge()
                            cursor.execute('UPDATE patient SET age = ? WHERE patientId = ?',(age,id))
                        except: 
                            print('Something went wrong')
                        else:
                            print('Age updated successfully')
                    case 4:
                        try:
                            bloodGroup = Utils.getBloodGroup()
                            cursor.execute('UPDATE patient SET bloodGroupId = ? WHERE patientId = ?',(bloodGroup,id))
                        except: 
                            print('Something went wrong')
                        else:
                            print('Blood Group updated successfully')
                    case 5: break
                    case _: print('Please Enter a valid option')
        else:
            print('No patient with this Id')            
    except Exception as e:
        print('Could not delete from database')
        print (e)


@dbConnect
def searchByName(cursor):
    name = Utils.getName("Enter the name of patient to be searched: ")
    name = f'%{name.title()}%'
    try: 
        cursor.execute('''SELECT patientId, patientName,genderName,age, bloodGroupName FROM patient 
        JOIN gender ON patient.genderId = gender.genderId 
        JOIN bloodGroup ON patient.bloodGroupId = bloodGroup.bloodGroupId WHERE patientName LIKE ? ''',(name))
        patients = cursor.fetchall()
        if len(patients) > 0:
            print('Patient found! ')
            myTable = PrettyTable(["Patient Id","Name", "Gender", "Age", "Blood group"])
            for patient_id, name, gender, age, bloodGroup in patients:
                myTable.add_row([patient_id, name, gender, age, bloodGroup])
            print(myTable)
        else: 
            print('No patient with this name!')
    except Exception as e:
        print('Something went wrong')
        print (e)

@dbConnect
def deletePatient(cursor):
    listAllPatients()
    id = Utils.getInt("Enter the id of patient to be deleted: ")
    try: 
        cursor.execute('DELETE FROM patient WHERE patientId = ?',(id))
    except Exception as e:
        print('Could not delete from database')
        print (e)
    else:
        if cursor.rowcount > 0:
            print('Patient deleted successfully')
        else:
            print('Patient Id does not exist in database')

@dbConnect
def addPatient(cursor):
    name = Utils.getName("Enter Patient Name: ")
    name = name.title()
    gender = Utils.getGender()
    age = Utils.getAge()
    bloodGroup = Utils.getBloodGroup()
    try: 
        cursor.execute('INSERT INTO patient(patientName, genderID, age, bloodGroupId) VALUES(?,?,?,?)',(name,gender,age,bloodGroup))
    except Exception as e:
        print('Something went wrong')
        print (e)
    else: 
        print('Patient added successfully')

@dbConnect
def listAllPatients(cursor):
    try:
        cursor.execute('''SELECT patientId, patientName,genderName,age, bloodGroupName FROM patient 
        JOIN gender ON patient.genderId = gender.genderId 
        JOIN bloodGroup ON patient.bloodGroupId = bloodGroup.bloodGroupId''')
        patients = cursor.fetchall()
        if len(patients) > 0:
            print('Patient Details are: ')
            myTable = PrettyTable(["Patient Id","Name", "Gender", "Age", "Blood group"])
            for patient_id, name, gender, age, bloodGroup in patients:
                myTable.add_row([patient_id, name, gender, age, bloodGroup])
            print(myTable)
        else: 
            print('No patient records!')
    except:
        print('Something went wrong')


while(True):
    print("""Enter your required option:
    1. Add Patient
    2. Update Details
    3. Delete a patient
    4. List Patients
    5. Search Patients
    6. Exit
    """)
    option = Utils.getInt()
    match(option):
        case 1: addPatient()
        case 2: updatePatient()
        case 3: deletePatient()
        case 4 : listAllPatients()
        case 5: searchByName()
        case 6: exit()
        case _: print("Invalid option")
            
