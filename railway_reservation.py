import pyodbc
import functools
conString = 'Driver={SQL Server};Server=CPU1213\SQLEXPRESS;Database=camp2;Trusted_Connection=yes;'

def dbConnect(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            myconn = pyodbc.connect(conString)
            cursor = myconn.cursor()
            myFunc(cursor,*args)
            myconn.commit()
            myconn.close()
        except:
            print('Connection error')
    return innerWrapper

@dbConnect
def getListAllStops(cursor):
    cursor.execute('SELECT * FROM stops')
    print(cursor.fetchall())



listAllStops()