import os
import psycopg2
import psycopg2.extras
from config import db_connection

def get_all_expenses():
    conn = db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Insert data into the table

    cur.execute('select * from expense_list;')
    expense_all = cur.fetchall()
    expenses = []
    for expense in expense_all:
        expenses.append(dict(expense))
    cur.close()
    conn.close()

    return expenses

