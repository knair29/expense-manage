from flask import Flask, render_template, request,redirect
from database import get_all_expenses,get_expense_by_id,get_all_currs,get_all_types,load_exp_db
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

@app.route('/create',methods=['get','post'])
def addexpense():
    print(request.method)
    if request.method=='POST':
        # insert expense into db
        res=load_exp_db(request.form)
        
        if(res):
            return redirect('/')
        else:
            return "Error while inserting DB",
    else:
        # load exp type from db
        exp_types = get_all_types()

        # load curr from db
        currs = get_all_currs()
        return render_template('create_expense.html',exp_types=exp_types,currs=currs)
    
    


if __name__ == '__main__':
    app.run(debug=True)