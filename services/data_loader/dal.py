from sql_connection import DataLoader


class Dall:
    def __init__(self):
        data = DataLoader()
        self.connection = data.connection

    def select(self, table_name):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()



