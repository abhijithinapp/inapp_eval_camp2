from gzip import READ
from tkinter.tix import Select
import pyodbc
import functools
conString = 'Driver={SQL Server};Server=CPU1213\SQLEXPRESS;Database=camp2;Trusted_Connection=yes;'
MAX_BIRTH_IN_TRAIN = 5
MAX_WL_IN_TRAIN = 2
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
    def getName(*msg):
        while(True):
            value = input(*msg)
            if len(value) <= MAX_LENGTH_OF_NAME_ALLOWED_IN_DB:
                return value
            else:
                print("Maximum charaxters allowed is 50")
                continue

def dbConnect(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            myconn = pyodbc.connect(conString)
            cursor = myconn.cursor()
            result = myFunc(cursor,*args)
            myconn.commit()
            myconn.close()
            return result
        except Exception as e:
            print('Connection error')
            print(e)
    return innerWrapper

@dbConnect
def getListAllStops(cursor):
    cursor.execute('SELECT * FROM stops')
    stops = cursor.fetchall()
    return stops

@dbConnect 
def bookTicket(cursor, stopId, name):
    cursor.execute('SELECT * FROM trains WHERE end_id >= ?',(stopId))
    trains = cursor.fetchall()
    bookedStatus = False
    for trainId,trainName,_,birthFilled,_ in trains:
        if birthFilled < MAX_BIRTH_IN_TRAIN:
            cursor.execute('INSERT INTO passengerdetails(passenger_name,stop_id,train_id) VALUES (?,?,?);',(name,stopId,trainId))
            cursor.execute('UPDATE trains SET birth_filled = ? WHERE train_id = ?',(birthFilled+1,trainId))
            bookedStatus = True
            print(f'{trainName} available! Booking successfull')
            return bookedStatus
    return bookedStatus

@dbConnect 
def addtoWaitingList(cursor, stopId, name):
    cursor.execute('SELECT * FROM trains WHERE end_id >= ?',(stopId))
    trains = cursor.fetchall()
    addtoWLStatus = False
    for trainId,trainName,_,_,waitingListFilled in trains:
        if waitingListFilled < MAX_WL_IN_TRAIN:
            cursor.execute('INSERT INTO waitlist(passenger_name,stop_id,train_id) VALUES (?,?,?);',(name,stopId,trainId))
            cursor.execute('UPDATE trains SET wait_list_filled = ? WHERE train_id = ?',(waitingListFilled+1,trainId))
            addtoWLStatus = True
            print(f'{trainName} available! Added to Waiting List')
            return addtoWLStatus
    return addtoWLStatus

@dbConnect
def showPassengerDetails(cursor):
    cursor.execute('''SELECT passenger_id, passenger_name, stop, train_name  FROM passengerdetails 
    JOIN stops ON passengerdetails.stop_id = stops.stop_id 
    JOIN trains ON passengerdetails.train_id = trains.train_id ORDER BY passengerdetails.train_id''')
    print('Passenger Details are: ')
    passengers = cursor.fetchall()
    print('Passenger Id     name    stop    train_name')
    for passenger_id, name, stop, train_name in passengers:
        print(f'{passenger_id}  {name}  {stop}  {train_name}')

@dbConnect
def showWLDetails(cursor):
    cursor.execute('''SELECT passenger_id, passenger_name, stop, train_name  FROM waitlist 
    JOIN stops ON waitlist.stop_id = stops.stop_id 
    JOIN trains ON waitlist.train_id = trains.train_id ORDER BY waitlist.train_id''')
    print('waiting list Details are: ')
    passengers = cursor.fetchall()
    print('Passenger Id     name    stop    train_name')
    for passenger_id, name, stop, train_name in passengers:
        print(f'{passenger_id}  {name}  {stop}  {train_name}')


def bookorAddtoWL():
    stations = getListAllStops()
    print('\nYou can board from Trivandrum. Below are destination stations')
    for stationcode, stationname in stations:
        if stationcode!=0:
            print(stationcode, stationname)
    destination = Utils.getInt("For booking, enter number of the destination station: ")
    name = Utils.getName('Enter your name: ')
    if not bookTicket(destination,name):
        option = input('No trains available to book. Do you want to added to waiting list of available train(y/n)')
        match(option):
            case 'y': 
                if not addtoWaitingList(destination,name):
                    print("No trains to available to be added to waiting list! Thankyou for chosing our service")
                    return
            case 'n': print("Sorry to hear that! Thankyou for choosing our service")


while(True):
    choice = Utils.getInt('''
    Choose an option
    1. Book a ticket
    2. View Passenger details
    3. View waiting list details:
    4. Exit
    ''')
    match(choice):
        case 1 : bookorAddtoWL()
        case 2 : showPassengerDetails()
        case 3 : showWLDetails()
        case 4 : exit()
        case _ : print('Invalid input')
        

