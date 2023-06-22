from flask import Flask, render_template
from database import get_all_expenses
app = Flask(__name__)

@app.route('/')
def load():
    EXPENSES = get_all_expenses()
    print(type(EXPENSES))
    return render_template('home.html',expenses=EXPENSES)


if __name__ == '__main__':
    app.run(debug=True)