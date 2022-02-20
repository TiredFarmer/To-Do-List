from flask import request, render_template, redirect
from todoapp import app
from todoapp.models import add_user, auth_user


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/create_account")
def create_account_page():
    return render_template("create_account.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/create_account", methods=["POST"])
def account_creation():
    username = request.form['username']
    password = request.form['password']

    print(username, password)

    if add_user(username, password):
        return render_template("account_creation_success.html")
    else:
        return render_template("username_already_taken.html")


@app.route("/", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username, password)

    if auth_user(username, password):
        print("authenticated")
        return render_template("todo.html")
    else:
        print("bad pass")
        return render_template("invalid_login.html")

    print(current_user)


@app.route("/todo", methods=["POST"])
def todo_add():
    course = request.form['Course']
    asmt = request.form['ASMT']
    date = request.form['Date']
    print(course, asmt, date)
