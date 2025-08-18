from request_data_loader import Request
class Menu:
    def __init__(self):
        self.db_request = Request('http://data-loader-goldflam-dev.apps.rm2.thpm.p1.openshiftapps.com')

    def menu(self):
        flag = True
        while flag:
            match input('Choose one of the options below: \n1. Update the table name \n2. insert new row \n3. Predict a row\nany key to Exit:\n4. select data for prediction \nEnter your choice: \n'):
                case '1':
                    table_name = input('Enter the table name: ')
                    self.db_request.select_table(table_name)

                case '2':
                    table_name = input('Enter the table name: ')
                    columns = input('Enter the columns: ')
                    new_row = input('Enter the new row: ')
                    self.db_request.insert_new_row(table_name, columns, new_row)

                # case '3':
                #     row_dict = eval(input('enter row dict: '))
                #     model_name = input('Enter the model name: ')
                #     self.classify_request.predict_row_request((row_dict, model_name))
                # #!!!!!!!!!!!!!!!!!!!!!!!!
                # case '4':
                #     data_name = input('Enter the data name: ')
                #     self.classify_request.select_data(data_name)

                case _:
                    flag = False
a = Menu()
a.menu()