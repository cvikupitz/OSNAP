"""
app.py
Author: Cole Vikupitz
CIS 322 Assignment 6
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return ""


@app.route('/create_user', methods = ['GET','POST'])
def create_user():
    if (request.method == 'GET'):
        return render_template("create_user.html")
    else:
        return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return ""

@app.route('/logout')
def logout():
    return ""

	
if __name__ == "__main__":
    app.run()
