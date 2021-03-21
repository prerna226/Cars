from django.db import connection
from decouple import config
import psycopg2

class QueryBuilder():
    ps_connection = psycopg2.connect(user=config('DATABASE_USER'),
                                     password=config('DATABASE_PASSWORD'),
                                     host=config('DATABASE_HOST'),
                                     port=config('DATABASE_PORT'),
                                     database=config('DATABASE_NAME'))

    cursor = ps_connection.cursor()

    def __init__(self):
        try:
            self.ps_connection = psycopg2.connect(user=config('DATABASE_USER'),
                                     password=config('DATABASE_PASSWORD'),
                                     host=config('DATABASE_HOST'),
                                     port=config('DATABASE_PORT'),
                                     database=config('DATABASE_NAME'))
            self.cursor = self.ps_connection.cursor()
        except BaseException as e:
            print(str(e))

    def dispose(self):
        try:
            self.ps_connection.commit()
            self.cursor.close()
        except BaseException as e:
            print(str(e))
            try:
                self.ps_connection.close()
            except BaseException as e:
                print(str(e))

    def closeConnection(self):
        try:
            self.cursor.close()
            self.ps_connection.close()
        except BaseException as e:
            print(str(e))

    def commit(self):
        try:
            self.conn.commit()
        except BaseException as e:
            print(str(e))

        
       
            
        
                

        
       