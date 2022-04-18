#
# class for open connection to mysql
#

# libs
import mysql.connector
from os.path import isfile


class Mysql_Connect:

    # constructor
    def __init__(self, path_to_config: str = "configs/db.conf"):

        # config dict
        configs = self.Load_Configs(path_to_config)

        # set values
        self.host = configs['db_addr']
        self.user = configs['db_user']
        self.password = configs['db_password']
        self.db = configs['db_name']

    # method for load db config
    def Load_Configs(self, path_to_config: str):   
        try:
            if (isfile(path_to_config)):
                # create dict from file
                return dict(map(lambda line: line.replace("\n","").split("="),open(path_to_config,"r").readlines()))
            else:
                # show error
                raise Exception("DB config file '%s' is not defined" % (path_to_config))
        except:
            raise Exception("DB config file '%s' is not defined or parsing error" % (path_to_config))




    # method for open db connection
    def Connect(self):
        try:
            # create connection and cursor
            self.connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.db)
            self.cursor = self.connection.cursor()

        except:
            print("DB can not open connection")

    # method for close db connection
    def Disconnect(self):
        try:
            # Close cursor and connection
            self.cursor.close()
            self.connection.close()

        except:
            print("DB can not close connection")

    # Method for send data to db
    def Insert(self, sql_command, *data):
        try:
            # Open connection
            self.Connect()

            # exec command commit data and read result
            self.cursor.execute(sql_command, data)

            # make commit
            self.connection.commit()

            # Close connection
            self.Disconnect()

        except:
            print(sql_command)
            print("DB sql querry error")

    # Method for load first record from db
    def Fetch_All(self, sql_command, *data):
        try:
            # Open connection
            self.Connect()

            # exec command commit data and read result
            self.cursor.execute(sql_command, data)

            # read response
            db_response = self.cursor.fetchall()

            # Close connection
            self.Disconnect()

            # return result
            return db_response

        except:
            print(sql_command)
            print("DB sql querry error")
