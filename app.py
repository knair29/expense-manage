from flask import Flask, render_template, request,redirect
from database import get_all_expenses,get_expense_by_id,get_all_currs,get_all_types,load_exp_db,search_expense
app = Flask(__name__)

# load all expenses
@app.route('/')
def load():
    EXPENSES = get_all_expenses()
    print(type(EXPENSES))
    return render_template('home.html',expenses=EXPENSES)

# load expense by id
@app.route('/expense/<id>')
def loadid(id):
    EXPENSE = get_expense_by_id(id)
    if not EXPENSE:
        return "Record not found",404
    
    return render_template('expensedesc.html',expense=EXPENSE)

# create new expense and
# refresh expense
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
    
# search expense
@app.route('/search',methods=['get','post'])
def searchexpense():
# search from db
    if request.method=='GET':
        #res=search_expense(request.args.get('val'))
        #res=request.args.get('val')
        res=search_expense(request.args.get('exp_search'))
        expenses=res
        return render_template('home.html',expenses=res)
    else:
        return 'No records found'


if __name__ == '__main__':
    app.run(debug=True)