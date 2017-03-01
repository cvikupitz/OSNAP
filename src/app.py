"""
app.py
Author: Cole Vikupitz
CIS 322
"""

# Imports
from flask import *
from config import dbname, dbhost, dbport
from util import *
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
                cur.execute("SELECT r.name FROM roles r JOIN users u ON r.role_pk=u.role WHERE u.username=%s", entries[:1])
                session['role'] = cur.fetchone()[0]
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
        if ('username' in request.form and 'password' in request.form and 'confirm' in request.form and 'role' in request.form):
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
            cur.execute("SELECT name FROM roles WHERE role_pk=%s", entries[-1])
            session['role'] = cur.fetchone()[0]
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
    return render_template('dashboard.html', name = session['username'], role = session['role'])


"""
Sends the user to the facilities screen. Here, users can add
new facilities into the database, and view all the facilities in
the database.
"""
@app.route('/add_facility', methods = ['GET', 'POST'])
def add_facility():

    # Loads the facilities page.
    if (request.method == 'GET'):
        cur.execute("SELECT * FROM facilities")
        res = cur.fetchall()
        return render_template('add_facility.html', facilities = res)

    # User inserts a new facility into the database.
    else:
        if ('name' in request.form and 'code' in request.form):
            entries = (request.form['name'], request.form['code'])

            # If the facility entered has an existing name/code, notify user.
            cur.execute("SELECT * FROM facilities WHERE common_name=%s OR code=%s", entries)
            if (cur.fetchone() != None):
                session['message'] = "Duplicate Entry: There's already a facility with that name/code."
                return redirect(url_for('dashboard_redirect'))

            # Inserts the facility into the database.
            else:
                cur.execute("INSERT INTO facilities (common_name, code) VALUES (%s, %s)", entries)
                conn.commit()
                return redirect(url_for('add_facility'))
        else:
            abort(401)


"""
Sends the user to the assets screen. Here, users can add
new assets into the database, and view all the assets in
the database.
"""
@app.route('/add_asset', methods = ['GET', 'POST'])
def add_asset():
    
    # Loads the assets page.
    if (request.method == 'GET'):
        cur.execute("SELECT * FROM assets")
        res = cur.fetchall()
        cur.execute("SELECT * FROM facilities")
        res2 = cur.fetchall()
        return render_template('add_asset.html', assets = res, facilities = res2)

    # User enters an asset into the database.
    else:
        if ('tag' in request.form and 'desc' in request.form and 'facility' in request.form and 'date' in request.form):
            entries = (request.form['tag'], request.form['desc'], request.form['facility'], request.form['date'])

            # The asset tag already exists, redirect with error message.
            cur.execute("SELECT * FROM assets WHERE tag=%s", entries[:1])
            if (cur.fetchone() != None):
                session['message'] = "Duplicate Entry: There's already an asset with that tag."
                return redirect(url_for('dashboard_redirect'))

            # Check the date for validity
            if (not date_valid(entries[3])):
                session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                return redirect(url_for('dashboard_redirect'))

            # Inserts the asset into the database.
            else:
                cur.execute("INSERT INTO assets (tag, description) VALUES (%s, %s)", entries[:2])
                conn.commit()
                cur.execute("SELECT facility_pk FROM facilities WHERE common_name=%s", entries[2:3])
                ffk = cur.fetchone()[0]
                #cur.execute("SELECT asset_pk FROM assets WHERE tag=%s", entries[:1])
                #afk = cur.fetchone()[0]
                #date = date_to_string(entries[3])
                #cur.execute("INSERT INTO asset_status (asset_fk, facility_fk, arrive_date) VALUES (%s, %s, %s)",
                #        (afk, ffk, date))
                #conn.commit()
                print(ffk)
                return redirect(url_for('add_asset'))
        else:
            abort(401)


""""""
@app.route('/dispose_asset', methods = ['GET', 'POST'])
def dispose_asset():
    if (request.method == 'GET'):
        if (session['role'] != 'Logistics Officer'):
            session['message'] = "Page Restricted: Only logistics officers may access this page."
            return redirect(url_for('dashboard_redirect'))
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
Send the user to a page containing a message. This message
will be an error message describing the nature of the
redirection (i.e. duplicate entries). User will
be able to redirect back to the dashboard.
"""
@app.route('/dashboard_redirect', methods = ['GET', 'POST'])
def dashboard_redirect():
    # Go to message screen with message.
    return render_template('dashboard_redirect.html', message = session['message'])


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


