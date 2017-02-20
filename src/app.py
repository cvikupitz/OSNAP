"""
app.py
Author: Cole Vikupitz
CIS 322 Assignment 6
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():
    return render_template("login.html")


@app.route('/create_user', methods = ['GET','POST'])
def create_user():
    return render_template("create_user.html")


@app.route('/dashboard', methods = ['GET','POST'])
def create_user():
    return render_template("dashboard.html")

	
if __name__ == "__main__":
    app.run()
