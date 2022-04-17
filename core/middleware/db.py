#
# class for open connection to mysql
#

# libs
import mysql.connector


class Mysql_Connect:

    # constructor
    def __init__(self, host, user, password, db):

        self.host = host
        self.user = user
        self.password = password
        self.db = db

    # Output read server answer
    def Exec(self, sql_command:str, need_commit:bool = False, *data):
        try:
            # create connection and cursor
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.db)
            cursor = connection.cursor()

            # exec command commit data and read result
            cursor.execute(sql_command, data)

            # make commit if need
            if need_commit: connection.commit()

            # read response
            db_response = cursor.fetchall()

            # Close cursor and connection
            cursor.close()
            connection.close()

            return db_response

        except:
            print(sql_command)
            print("DB connection error")
            return None
