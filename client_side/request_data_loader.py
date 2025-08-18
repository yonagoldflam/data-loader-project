import requests


class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def select_table(self, table_name):
        response = requests.get(f"{self.base_url}/select/{table_name}")
        print(response.status_code)
        print(response.text)

    def insert_new_row(self,table_name,columns, new_row):
        response = requests.get(f"{self.base_url}/insert/{table_name}/{columns}/{new_row}")
        print(response.status_code)
        print(response.text)