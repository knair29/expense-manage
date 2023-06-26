from flask import Flask, render_template
from database import get_all_expenses,get_expense_by_id
app = Flask(__name__)

@app.route('/')
def load():
    EXPENSES = get_all_expenses()
    print(type(EXPENSES))
    return render_template('home.html',expenses=EXPENSES)

@app.route('/expense/<id>')
def loadid(id):
    EXPENSE = get_expense_by_id(id)
    if not EXPENSE:
        return "Record not found",404
    
    return render_template('expensedesc.html',expense=EXPENSE)




if __name__ == '__main__':
    app.run(debug=True)