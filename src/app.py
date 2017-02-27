"""
app.py
Author: Cole Vikupitz
CIS 322
"""

# Imports
from flask import *
from config import dbname, dbhost, dbport
import psycopg2

# Set up flask application
app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = "5a7c8059c6f4b390b06bcdbf81c03affdc67a3f8f0006c8e"
conn = psycopg2.connect(dbname = dbname, host = dbhost, port = dbport)
cur = conn.cursor()


"""
Login page for the users. User can login with a username
and password, and will link to dashboard if the login
was successful, or notify user if unsuccessful.
"""
@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():
    
    # Loads the login page
    if (request.method == 'GET'):
        return render_template('login.html')
    
    # User attempts login, get username and password, checks entries in database.
    else:
        if ('username' in request.form and 'password' in request.form):
            # Obtain the account from the database.
            entries = (request.form['username'], request.form['password'])
            cur.execute("SELECT username FROM USERS WHERE username=%s AND password=%s", entries)

            # Incorrect login, redirect to error message.
            if (cur.fetchone() == None):
                session['message'] = "Unauthenticated User: Incorrect username/password."
                return redirect(url_for('message'))

            # Successful login, go to dashboard.
            else:
                session['username'] = entries[0]
                return redirect(url_for('dashboard'))
        else:
            abort(400)


"""
Send the user to the create user screen. Here, users can
create a new account by giving a username and password
16 characters or less. Checks to see if the new info
exists and alerts users if so.
"""
@app.route('/create_user', methods = ['GET','POST'])
def create_user():

    # Loads the create user page.
    if (request.method == 'GET'):
        return render_template('create_user.html')
    
    # User creates a new account, creates the account or rejects the request.
    else:
        if ('username' in request.form and 'password' in request.form and 'confirm' in request.form):
            entries = (request.form['username'], request.form['password'],
                       request.form['confirm'], request.form['role'])

            # Password and confirmation must match.
            if (entries[1] != entries[2]):
                session['message'] = "Password Mismatch: Make sure that your passwords match."
                return redirect(url_for('message'))

            # Check to see if there already exists an account with the username.
            cur.execute("SELECT username FROM users WHERE username=%s", (entries[:1]))
            if (cur.fetchone() != None):
                session['message'] = "Occupied User: That username already exists."
                return redirect(url_for('message'))

            # Creates the new account, goes to the dashboard.
            cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                        (entries[0], entries[1], entries[3]))
            conn.commit()
            session['username'] = entries[0]
            session['role'] = entries[3]
            return redirect(url_for('dashboard'))

        else:
            abort(400)


"""
Send the user to the dashboard screen upon login. Displays
the username on the screen. User should be able to logout
from here.
"""
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    # Sign in to the dashboard.
    cur.execute("SELECT name FROM roles WHERE role_pk=%s", (session['role']))
    return render_template('dashboard.html', name = session['username'], role = cur.fetchone()[0])


""""""
@app.route('/add_facility', methods = ['GET', 'POST'])
def add_facility():
    if (request.method == 'GET'):
        cur.execute("SELECT * FROM facilities")
        res = cur.fetchall()
        return render_template('add_facility.html', facilities = res)
    else:
        if ('name' in request.form and 'code' in request.form):
            entries = (request.form['name'], request.form['code'])

            cur.execute("SELECT * FROM facilities WHERE common_name=%s AND code=%s", entries)
            if (cur.fetchone != None):
                alert("DUPLICATE")
                return

            cur.execute("INSERT INTO facilities (common_name, code) VALUES (%s, %s)", entries)
            conn.commit()
            return redirect(url_for('add_facility'))
        else:
            abort(401)


""""""
@app.route('/add_asset', methods = ['GET', 'POST'])
def add_asset():
    if (request.method == 'GET'):
        return render_template('add_asset.html')
    else:
        ####
        return render_template('add_asset.html')


""""""
@app.route('/dispose_asset', methods = ['GET', 'POST'])
def dispose_asset():
    if (request.method == 'GET'):
        return render_template('dispose_asset.html')
    else:
        ####
        return render_template('dispose_asset.html')


""""""
@app.route('/asset_report', methods = ['GET', 'POST'])
def asset_report():
    if (request.method == 'GET'):
        return render_template('asset_report.html')
    else:
        ####
        return render_template('asset_report.html')


"""
Send the user to a page containing a message. This message
will be an error message describing the nature of the
redirection (i.e. username and password incorrect). User will
be able to redirect back to the login page.
"""
@app.route('/message', methods = ['GET', 'POST'])
def message():
    # Go to message screen with message.
    return render_template('message.html', message = session['message'])


"""
User has logged out of the system, go to the logout page, link
user back to the login page upon request.
"""
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    # Pop out username from session, go to logout screen.
    session.pop('username', None)
    return render_template('logout.html')


# Starts and runs the application.
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)


