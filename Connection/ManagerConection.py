from decouple import config
from psycopg2 import connect

class ManagerConection:
    def __init__(self):
        try:
            conn = connect(
                host = config('POSTGRES_HOST'),
                port = config('POSTGRES_PORT'),
                database = config('POSTGRES_DB'),
                user = config('POSTGRES_USER'),
                password = config('POSTGRES_PASS')
            )
        except expression as identifier:
            print('Error 500 - Impossible to connect {}'.format(identifier))
