import os
import psycopg2


db = psycopg2.connect(
            host= os.environ['host'],
            database=os.environ['database'],
            user = os.environ['user'],
            password = os.environ['password'])


def db_connection():
    db_conn = psycopg2.connect(
            host= os.environ['host'],
            database=os.environ['database'],
            user = os.environ['user'],
            password = os.environ['password'])
    return db_conn