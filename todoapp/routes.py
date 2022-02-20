from flask import request, render_template
from todoapp import app
from todoapp.models import User, Assignment


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")


'''
#account creation 
# '''


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/", methods=["POST"])
def account_creation():
    text = request.form['text']

    ''' back end
    if account_creation(processed_text):
        return render_template("todo.html")
    '''

    if text == "your mom":
        return render_template("login.html")
    if text == "todo":
        return render_template("todo.html")
    return render_template("create_account.html")


@app.route("/login.html", methods=["POST"])
def login_attempt():
    text = request.form['text']
    '''back end
    if login(processed_text)
        return render_template("todo.html)
    '''
    return render_template("login.html")


@app.route("/todo", methods=["POST"])
def todo_add():
    course = request.form['Course']
    asmt = request.form['ASMT']
    date = request.form['Date']
    print(course, asmt, date)