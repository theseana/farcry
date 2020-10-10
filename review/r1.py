import mysql.connector


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
        db='schoolManagement',
        user='root',
        password='',
        host='localhost',
        )

        self.cursor = self.db.cursor()

