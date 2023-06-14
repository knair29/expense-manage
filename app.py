from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hellowrold():
    JOBS = [
        {
            "id":1,
            "ExpenseType":"Mortgage Loan",
            "Amount":"24000 Rs",
            "Date":"24/05/23",
        },
        {
            "id":2,
            "ExpenseType":"Credit Card Bill",
            "Amount":"20000 Rs",
            "Date":"29/05/23",
        },
        {
            "id":3,
            "ExpenseType":"Misc Expenses",
            "Amount":"15000 Rs",
            "Date":"30/05/23",
        },
    ]
    return render_template('home.html',jobs=JOBS)


if __name__ == '__main__':
    app.run(debug=True)