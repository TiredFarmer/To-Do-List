'''
Date: 2022-02-19

'''
from flask import Flask,request,render_template
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'super secret'

@app.route("/")
def home():
    return "Hello, Flask!"
   
