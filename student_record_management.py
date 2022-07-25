# 2. Student report card management system


class Student:
    def __init__(self, name, maths, physics, chemistry, english, programing) :
        self.__name       = name
        self.__maths      = maths
        self.__physics    = physics
        self.__chemistry  = chemistry
        self.__english    = english
        self.__programing = programing
    
    @property
    def name(self):
        return self.__name
    
    @property
    def maths(self):
        return self.__maths
    
    @property
    def physics(self):
        return self.__physics
    
    @property
    def chemistry(self):
        return self.__chemistry
    
    @property
    def english(self):
        return self.__english
    
    @property
    def programing(self):
        return self.__programing
    
    @maths.setter
    def maths(self, newMark):
        self.__maths = newMark
    
    @maths.setter
    def physics(self, newMark):
        self.__physics = newMark
    
    @maths.setter
    def chemistry(self, newMark):
        self.__chemistry = newMark
    
    @maths.setter
    def english(self, newMark):
        self.__english = newMark
    
    @maths.setter
    def programming(self, newMark):
        self.__programming = newMark

    def displayStudentDetails(self):
        print('Name :', self.__name)
        print('Marks:')
        print('Maths:', self.__maths)
        print('Physics:', self.__physics)
        print('Chemistry:', self.__chemistry)
        print('English:', self.__english)
        print('Programing:', self.__programing)


class StudentRecord:
    studentList = dict()

    @staticmethod
    def create():
        rollno = int(input('Rollno: '))
        if StudentRecord.studentList.get(rollno):
            print('This student already exists')
        else:
            name = input('Name: ')
            maths       = input('Enter Maths Marks: ')
            physics     = input('Enter Physics Marks: ')
            chemistry   = input('Enter Chemistry Marks: ')
            english     = input('Enter English Marks: ')
            programing  = input('Enter Programing Marks: ')
            student  = Student(name, maths, physics, chemistry, english, programing)
            StudentRecord.studentList[rollno] = student
            print('Student Records added!')
    
    @staticmethod
    def delete():
        rollno = int(input('Rollno: '))
        if StudentRecord.studentList.get(rollno):
            del  StudentRecord.studentList[rollno]
            print('Student deleted successfully')
        else:
            print('Student does not exist')
    
    @staticmethod
    def modify():
        rollno = int(input('Rollno: '))
        if  StudentRecord.studentList.get(rollno):
            student =  StudentRecord.studentList.get(rollno)
            student.displayStudentDetails()
            while(True):
                opt = int(input('''
Choose Mark to edit:
    1. Maths
    2. Physics
    3. Chemistry
    4. English
    5. Programing
    6. Exit
    '''
                ))
                match opt:
                    case 1: student.maths = input('Enter Maths mark ')
                    case 2: student.physics = input('Enter Physics Mark: ')
                    case 3: student.chemistry = input('Enter Chemistry Mark: ')
                    case 4: student.english = input('Enter English Marks: ')
                    case 5: student.programing = input('Enter Programing Marks: ')
                    case 6: break
                    case _: print('Invalid input')
        else:
            print('Student does not exist')

    @staticmethod
    def listAllStudents():
        if len( StudentRecord.studentList) > 0:
            print('Student details: ')
            for rollno, student in  StudentRecord.studentList.items():
                print('\nRollno: ', rollno)
                student.displayStudentDetails()
        else:
            print('No records ')

    @staticmethod
    def showStudentDetails():
        rollno = int(input('Enter Rollno: '))
        if StudentRecord.studentList.get(rollno):
            print('\nRollno: ', rollno)
            StudentRecord.studentList[rollno].displayStudentDetails()
        else:
            print('Student does not exist')
    

while(True):
    opt = int(input('''
    1. Create Student Record
    2. Delete Student Record
    3. Modify Marks
    4. Display all Students
    5. Display a student record
    6. Exit
    '''))

    match opt:
        case 1: StudentRecord.create()
        case 2: StudentRecord.delete()
        case 3: StudentRecord.modify()
        case 4: StudentRecord.listAllStudents()
        case 5: StudentRecord.showStudentDetails()
        case 6: break
        case _: print('Invalid input')