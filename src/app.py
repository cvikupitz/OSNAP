"""
app.py
Author: Cole Vikupitz
CIS 322 Assignment 6
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


##@app.route('/login')
##def login():
##    return "Login...."
##
##
##@app.route('/filter')
##def filter():
##    return "Filter...."
##
##
##@app.route('/inventory')
##def inventory():
##    return "Inventory...."
##
##
##@app.route('/transit')
##def transit():
##    return "Transit...."
##
##
##@app.route('/logout')
##def logout():
##    return "Logout...."

	
if __name__ == "__main__":
    app.run()
