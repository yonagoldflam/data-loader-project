import mysql.connector
from mysql.connector import Error

class DataLoader:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                #!!!!!!!!!!!!!
                # need fix env
                host="localhost",
                user="root",
                password="",
                database="mydatabase"

            )
            if not self.connection.is_connected():
                raise Error("Error connecting to MySQL database")
        except Error as e:
            print(f'mysql connection error: {e}')

