"""
app.py
Author: Cole Vikupitz
CIS 322 Assignment 6
"""

# Imports
from flask import Flask, request, render_template

app = Flask(__name__)

"""
Login page for the users. User can login with a username
and password, and will link to dashboard if the login
was successful, or notify user if unsuccessful.
"""

##@app.route('/login', methods = ['GET','POST'])
##def login():
##    return """"""
##
##


"""
Send the user to the create user screen. Here, users can
create a new account by giving a username and password
16 characters or less. Checks to see if the new info
exists and alerts users if so.
"""
@app.route('/')
@app.route('/create_user', methods = ['GET','POST'])
def create_user():
    if (request.method == 'GET'):
        return render_template('create_user.html')
    else:
        ####### FIXME
        return render_template('login.html')


"""
Send the user to the dashboard screen upon login. Displays
the username on the screen. User should be able to logout
from here.
"""
@app.route('/dashboard/<user>', methods = ['GET'])
def dashboard(user):
    return render_template('dashboard.html', name = user)

"""
User has logged out of the system, go to the logout page, link
user back to the login page upon request.
"""
@app.route('/logout', methods = ['GET'])
def logout():
    return render_template('logout.html')

	
if __name__ == "__main__":
    app.run(debug = True)
