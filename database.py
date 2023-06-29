import os
import psycopg2
import psycopg2.extras
from config import db_connection

def get_all_expenses():
    conn = db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Insert data into the table

    cur.execute('select * from expense_list order by exp_id desc;')
    expense_all = cur.fetchall()
    expenses = []
    for expense in expense_all:
        expenses.append(dict(expense))
    cur.close()
    conn.close()

    return expenses

def get_expense_by_id(id):
    conn = db_connection()

    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    queryText = 'select * from expense_list where exp_id = %s'
    cur.execute(queryText,(id,))

    expense = cur.fetchall()

    cur.close()
    conn.close()

    if len(expense)<=0:
        return None

    return dict(expense[0])

# load all types from db
def get_all_types():
    conn = db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Insert data into the table

    cur.execute('select * from expense_type_master;')
    expense_types = cur.fetchall()
    exp_type_master = []
    for type in expense_types:
        exp_type_master.append(dict(type))
    cur.close()
    conn.close()

    return exp_type_master

  # load all currencies from db
def get_all_currs():
    conn = db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # select data into the table

    cur.execute('select * from expense_curr_master;')
    expense_curr = cur.fetchall()
    expenses_curr_master = []
    for curr in expense_curr:
        expenses_curr_master.append(dict(curr))
    cur.close()
    conn.close()

    return expenses_curr_master

# insert expenses into db
def load_exp_db(request):
    queryText = 'insert into expense_list (exp_type,exp_amount,exp_curr,exp_date,exp_desc) values (%s,%s,%s,%s,%s) RETURNING exp_id'
    print("load expense to db:",request.getlist('exp_type')[0])
    #get db connection
    conn = db_connection()

    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Insert data into db
    cur.execute(queryText,(request.getlist('exp_type')[0],request.getlist('exp_amount')[0],
                                            request.getlist('exp_curr')[0],request.getlist('exp_date')[0],request.getlist('exp_desc')[0]))

    res = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    print(res)
    if res>0:
        return 'true'
    else:
        return 'false'

#search expense from db:
def search_expense(request):
    #get db connection
    conn=db_connection()

    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    queryText = "select * from expense_list where exp_type ILIKE %s"
    cur.execute(queryText,('%'+request+'%',))
    res_all =  cur.fetchall()
   
    search_list = []
    for res in res_all:
        search_list.append(dict(res))
    
    cur.close()
    conn.close()
    print(search_list)
    return search_list