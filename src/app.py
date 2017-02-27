"""
app.py
Author: Cole Vikupitz
CIS 322 Assignment 6
"""

# Imports
from flask import *
from config import dbname, dbhost, dbport
import psycopg2

# Set up flask application
app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = "5a7c8059c6f4b390b06bcdbf81c03affdc67a3f8f0006c8e"
conn = psycopg2.connect(dbname = database, host = dbhost, dbport = port)
cur = conn.cursor()


"""
Login page for the users. User can login with a username
and password, and will link to dashboard if the login
was successful, or notify user if unsuccessful.
"""
@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():
    if (request.method == 'GET'):
        return render_template('login.html')
    else if (request.method == 'POST'):
        if ('username' in request.form and 'password' in password.form):
            un = request.form['username']
            pw = request.form['password']
            res = cur.execute("SELECT COUNT(*) FROM USERS WHERE username=%s AND password=%s", (un, pw))


        return """"""
    else:
        abort(401)


"""
Send the user to the create user screen. Here, users can
create a new account by giving a username and password
16 characters or less. Checks to see if the new info
exists and alerts users if so.
"""
@app.route('/create_user', methods = ['GET','POST'])
def create_user():
    if (request.method == 'GET'):
        return render_template('create_user.html')
    else:
        ####### FIXME #######
        return render_template('create_user.html')


"""
Send the user to the dashboard screen upon login. Displays
the username on the screen. User should be able to logout
from here.
"""
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html', name = session['username'])


"""
Send the user to a page containing a message. This message
will be an error message describing the nature of the
redirection (i.e. username and password incorrect). User will
be able to redirect back to the login page.
"""
@app.route('/message', methods = ['GET', 'POST'])
def message(msg):
    return render_template('message.html', message = msg)


"""
User has logged out of the system, go to the logout page, link
user back to the login page upon request.
"""
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    return render_template('logout.html')

	
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)


