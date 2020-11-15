from decouple import config
import time
import psycopg2

class ManagerConection:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname = config('POSTGRES_DB'),
                user = config('POSTGRES_USER'),
                password = config('POSTGRES_PASSWORD'),
                host = config('POSTGRES_HOST'),
                port = config('POSTGRES_PORT')
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
        except:
            print('Error 500 - Impossible to connect')

        
    def creating_table(self):
        sql_create = "CREATE TABLE IF NOT EXISTS public.test(id integer primary key, name varchar(100))"
        print("Testing Creation ")
        self.cursor.execute(sql_create)
        time.sleep(2)
        self.insert_data()
    
    def insert_data(self):
        sql_insert = "INSERT INTO test (id, name) values (1, 'test');"
        print("Testing Insert ")
        self.cursor.execute(sql_insert)
        time.sleep(2)
        self.select_table()
    
    def select_table(self):
        self.cursor.execute("SELECT * FROM test;")
        result = self.cursor.fetchall()
        print("Testing Select {} ".format(result[0]))
        time.sleep(5)
        self.delete_table()

    def delete_table(self):
        sql_delete = "DELETE FROM test"
        print("Testing Delete ")
        time.sleep(2)
        print("It's working!")


connection = ManagerConection()
connection.creating_table()

