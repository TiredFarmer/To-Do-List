'''
Date: 2022-02-19

'''
from flask import Flask,request,render_template,redirect
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'super secret'


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")


'''
#account creation 
# '''

@app.route("/")
def home():
    return render_template("create_account.html")

@app.route("/", methods = ["POST"]) 
def account_creation():
    text = request.form['text']

    
    ''' back end
    if account_creation(proccessed_text):
        return render_template("todo.html")
    '''
    
    if text == "your mom":
        return render_template("login.html") 
    if text == "todo":
        return render_template("todo.html")
    return render_template("create_account.html")



@app.route("/login.html", methods = ["POST"])
def login_attempt():
    text = request.form['text']
    '''back end
    if login(processed_text)
        return render_template("todo.html)
    '''
    return render_template("login.html")


@app.route("/todo", methods = ["POST"])
def todo_add():
    course = request.form['Course']
    asmt = request.form['ASMT']
    date = request.form['Date']
    print(course,asmt,date)


5
