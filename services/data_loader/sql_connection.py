import mysql.connector
import os
# from dotenv import load_dotenv

class DataLoader:
    def __init__(self):
        # load_dotenv()
        self.connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )