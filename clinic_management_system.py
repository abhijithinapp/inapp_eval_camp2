# Clinic management System
from contextlib import nullcontext
import itertools
from select import select
from sys import flags
from this import d


class Patient:

    def __init__(self, patientId, name, gender, age, dob, bloodGroup):

        self.patientId = patientId
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.bloodGroup = bloodGroup

    def showPatientDetails(self):
        print("""Patient ID: {}
Name: {}
Gender: {}
Age: {}
DOB: {}
Blood Group: {}""".format(self.patientId, self.name,
           self.gender,
           self.age,
           self.dob,
           self.bloodGroup))

    def updateDetails(self, name, gender, age, dob, bloodGroup):
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.bloodGroup = bloodGroup

class OP(Patient):
    def __init__(self, patientId, name, gender, age, dob, bloodGroup, disease, noOfDays):
        super().__init__(patientId, name, gender, age, dob, bloodGroup)
        self.disease = disease
        self.noOfDays = noOfDays
    
    def showInPatientDetails(self):
        self.showPatientDetails()
        print('Disease: {}'.format(self.disease))
        print('No of Days {}'.format(self.noOfDays))
  

class CMS:
    patientList = []
    nextPatientid = 1
    inPatientList = []
    opTicket = 1
    def register(self):
        name = input("\nEnter name: ")
        gender = input("Enter Gender(M/F): ")
        age = int(input("Enter Age: "))
        dob = input("Enter date of birth (dd-mm-yy): ")
        bloodGroup = input("Enter Blood group: ")
        patient = Patient(self.nextPatientid, name,
                          gender, age, dob, bloodGroup)
        self.patientList.append(patient)
        self.nextPatientid += 1
        print("\nPatient details added")

    def listPatients(self):
        print("\nPatient Details are: ")
        for patient in self.patientList:
            patient.showPatientDetails()

    def listOfAdmittedPatients(self):
        for patient in self.inPatientList:
            patient.showInPatientDetails()

    def search(self):
        flag = 0
        patientID = int(input("Enter patient ID to be searched: "))
        for patient in self.patientList:
            if patient.patientId == patientID:
                print("Details of patient with ID {}:".format(patientID))
                patient.showPatientDetails()
                flag = 1
        if flag == 0:
            print("Patient ID not found")
    
    def admit(self):
        flag = 0
        patientID = int(input("Enter patient ID to be searched: "))
        for patient in self.patientList:
            if patient.patientId == patientID:
                print("Details of patient with ID {}:".format(patientID))
                disease = input("Enter the disease")
                noOfDays = input("Enter the number of days to be admitted")
                outpatient = OP(patient.patientId,patient.name, patient.gender, patient.age, patient.dob, patient.bloodGroup,disease,noOfDays)
                self.inPatientList.append(outpatient)
                flag = 1
        if flag == 0:
            print("Patient ID not found")

    def delete(self):
        flag = 0
        patientID = int(input("Enter patient ID to be deleted: "))
        for patient in self.patientList:
            if patient.patientId == patientID:
                self.patientList.remove(patient)
                flag = 1
        if flag == 0:
            print("Patient details deleted")

    def generateOPTicket(self):
        print("OP ticket: {}".format(self.opTicket))
        self.opTicket += 1

    def UpdatePatientDetails(self):
        flag = 0
        patientID = int(input("Enter patient ID to be updated: "))
        for patient in self.patientList:
            if patient.patientId == patientID:
                name = input("\nEnter new name: ")
                gender = input("Enter new Gender(M/F): ")
                age = int(input("Enter new Age: "))
                dob = input("Enter new date of birth (dd-mm-yy): ")
                bloodGroup = input("Enter new Blood group: ")
                patient.updateDetails(name, gender, age, dob, bloodGroup)
                flag = 1
        if flag == 0:
            print("Patient ID not found")

        

cms = CMS()
while(1):
    option = int(input("""
Choose the required option
1. Register a Patient
2. List Patients
3. Search a patient
4. Delete a patient
5. Admit a Patient
6. List all admitted patients
7. Create OP Ticket
8. exit
"""))

    match(option):
        case 1: cms.register()
        case 2: cms.listPatients()
        case 3: cms.search()
        case 4: cms.delete()
        case 5: cms.admit()
        case 6: cms.listOfAdmittedPatients() 
        case 7: cms.generateOPTicket()
        case 8: exit()