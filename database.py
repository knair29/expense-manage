import os
import psycopg2
import psycopg2.extras



def get_all_expenses():
    conn = psycopg2.connect(
        host="localhost",
        database="expenses",
        #user=os.environ['DB_USERNAME'],
        #password=os.environ['DB_PASSWORD'])
        user = "expense_admin",
        password = "admin")
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

    print(type(expenses))
    return expenses


exp_type = get_all_expenses()
print(exp_type)
