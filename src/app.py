"""
app.py
Author: Cole Vikupitz

Flask application that runs the L.O.S.T. website.

For assignment 10:
    Web service done in two different service calls:
    /create_user - Activates or creates a user account.
    /revoke_user - Deactivates a user account, preventing login.
"""

# Imports
from flask import *
from util import *
from psql import *

# Set up flask application
app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY'] = "5a7c8059c6f4b390b06bcdbf81c03affdc67a3f8f0006c8e"


"""
Login page for the users. User can login with a username
and password, and will link to dashboard if the login
was successful, or notify user if unsuccessful.
"""
@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET','POST'])
def login():

    # Loads the login page
    if (session.get('message') == None):
        session['message'] = ""
    if (request.method == 'GET'):
        msg = session['message']
        session['message'] = ""
        return render_template('login.html', message = msg)

    # User attempts login, get username and password, checks entries in database.
    elif (request.method == 'POST'):
        if ('username' in request.form and 'password' in request.form):
            # Obtain the account from the database.
            entries = (request.form['username'], request.form['password'])

            # Incorrect login, redirect to error message.
            if (not authenticate(entries[0], entries[1])):
                session['message'] = "Unauthenticated User: Incorrect username/password."
                return redirect(url_for('login', message = session['message']))

            # Successful login, go to dashboard.
            else:
                session['username'] = entries[0]
                session['role'] = fetch_role(entries[0])
                return redirect(url_for('dashboard'))
    else:
        session['message'] = "Unauthenticated User: Incorrect username/password."
        return redirect(url_for('login', message = session['message']))


"""
Used for the web service to activate users for the L.O.S.T.
database. A username and password are given to create a new
account if the username is unique, or activates and replaces
the account's password.
"""
@app.route('/create_user', methods = ['POST'])
def create_user():

    if (request.method == 'POST'):
        # Create user if it does not exist.
        if not user_exists(request.form['username']):
            create_account(request.form['username'], request.form['password'], request.form['role'])

        # If user does exist, then replace password and activate.
        else:
            activate_account(request.form['username'], request.form['password'])
        return "-- Successfully activated the user " + request.form['username']

    else:
        return "Something went wrong, activation failed."


"""
Used for the web service to deactivate users for the L.O.S.T.
database. A username is given to disable the account. If the
username given does not exist, nothing should happen.
"""
@app.route('/revoke_user', methods = ['POST'])
def revoke_user():

    if (request.method == 'POST'):
        # If the user does not exist, do nothing.
        if not user_exists(request.form['username']):
            return "-- Deactivation failed, that username does not exist."

        # Sets the account's active flag to false.
        else:
            deactivate_account(request.form['username'])
            return "-- Successfully deactivated the user " + request.form['username']
    else:
        return "Something went wrong, deactivation failed."


"""
Send the user to the dashboard screen upon login. Displays
the username on the screen. User should be able to logout
from here.
"""
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    # Sign in to the dashboard.
    session['message'] = ""
    if (session['role'] == "Facilities Officer"):
        pending = get_pending_requests()
    else:
        pending = get_approved_requests()
    return render_template('dashboard.html', name = session['username'], role = session['role'], requests = pending)


"""
Sends the user to the facilities screen. Here, users can add
new facilities into the database, and view all the facilities in
the database.
"""
@app.route('/add_facility', methods = ['GET', 'POST'])
def add_facility():

    # Loads the facilities page.
    if (request.method == 'GET'):
        msg = session['message']
        session['message'] = ""
        return render_template('add_facility.html', message = msg, facilities = get_facilities())

    # User inserts a new facility into the database.
    else:
        if ('name' in request.form and 'code' in request.form):
            entries = (request.form['name'], request.form['code'])

            # Facility name cannot be only whitespace
            if (entries[0].isspace()):
                session['message'] = "Invalid Name: Facility names must contain characters."
                return redirect(url_for('add_facility'))

            # Facility codes may not contain whitespace
            if (' ' in entries[1]):
                session['message'] = "Invalid Code: Facility codes may not contain any spaces."
                return redirect(url_for('add_facility'))

            # If the facility entered has an existing name/code, notify user.
            if (facility_exists(entries[0], entries[1])):
                session['message'] = "Duplicate Entry: There's already a facility with that name/code."
                return redirect(url_for('add_facility'))

            # Inserts the facility into the database.
            else:
                create_facility(entries[1], entries[0])
                return redirect(url_for('add_facility'))
        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Sends the user to the assets screen. Here, users can add
new assets into the database, and view all the assets in
the database.
"""
@app.route('/add_asset', methods = ['GET', 'POST'])
def add_asset():

    # Loads the assets page.
    if (request.method == 'GET'):
        msg = session['message']
        session['message'] = ""
        return render_template('add_asset.html', message = msg, assets = get_assets(),
                               facilities = get_facilities())

    # User enters an asset into the database.
    else:
        if ('tag' in request.form and 'desc' in request.form and 'facility' in request.form and 'date' in request.form):
            entries = (request.form['tag'], request.form['desc'], request.form['facility'], request.form['date'])

            # The asset tag already exists, redirect with error message.
            if (asset_exists(entries[0])):
                session['message'] = "Duplicate Entry: There's already an asset with that tag."
                return redirect(url_for('add_asset'))

            # Check the date for validity
            if (not date_valid(entries[3])):
                session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                return redirect(url_for('add_asset'))

            # Check for white space in the asset tag, not allowed.
            if (' ' in entries[0]):
                session['message'] = "Invalid Tag: Asset tags may not contain any spaces."
                return redirect(url_for('add_asset'))

            # Inserts the asset into the database.
            else:
                create_asset(entries[0], entries[1], entries[2], entries[3])
                return redirect(url_for('add_asset'))
        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Sends the user to the asset disposure screen. Users can remove
assets from their facilities given a date they left.
"""
@app.route('/dispose_asset', methods = ['GET', 'POST'])
def dispose_asset():

    # Loads the asset disposure page.
    if (request.method == 'GET'):
        if (session['role'] != 'Logistics Officer'):
            session['message'] = "Page Restricted: Only logistics officers may access this page."
            return redirect(url_for('error'))
        msg = session['message']
        session['message'] = ""
        return render_template('dispose_asset.html', message = msg)

    # Removes the asset from the asset.
    else:
        if ('tag' in request.form and 'date' in request.form):
            entries = (request.form['tag'], request.form['date'])

            # Make sure the date is valid.
            if (not date_valid(entries[1])):
                session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                return redirect(url_for('dispose_asset'))

            # Check to see if the asset is in the system.
            if (not asset_exists(entries[0])):
                session['message'] = "Asset Not Found: The asset you entered does not exist."
                return redirect(url_for('dispose_asset'))

            # Check to see if the asset is already disposed.
            if (asset_disposed(entries[0])):
                session['message'] = "Disposed Asset: The asset you entered has already been disposed."
                return redirect(url_for('dispose_asset'))

            # Remove the asset from the system.
            dispose(entries[0], entries[1])
            return redirect(url_for('dispose_asset'))
        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Sends the user to the asset report screen. users can view
a summary of all assets contained at a facility on a given
date.
"""
@app.route('/asset_report', methods = ['GET', 'POST'])
def asset_report():

    # Loads the asset report page.
    if (session.get('report') == None):
        session['report'] = list()
    if (request.method == 'GET'):
        msg = session['message']
        session['message'] = ""
        rprt = session['report']
        session['report'] = list()
        return render_template('asset_report.html', message = msg, facilities = get_facilities(),
                               report = rprt)

    else:
        if ('facility' in request.form and 'date' in request.form):
            entries = (request.form['facility'], request.form['date'])

            # Make sure date is valid.
            if (not date_valid(entries[1])):
                session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                redirect(url_for('asset_report'))

            # Generate the report.
            session['report'] = generate_report(entries[0], entries[1])
            return redirect(url_for('asset_report'))

        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Sends the user to the transfer request page. Here, logistics
officers can submit transfer requests to other facility
officers to approve.
"""
@app.route('/transfer_req', methods = ['GET', 'POST'])
def transfer_req():

    # Loads the transfer request page.
    if (request.method == 'GET'):
        if (session['role'] != 'Logistics Officer'):
            session['message'] = "Page Restricted: Only logistics officers may access this page."
            return redirect(url_for('error'))
        msg = session['message']
        session['message'] = ""
        return render_template('transfer_req.html', message = msg, src_facilities = get_facilities(),
                dest_facilities = get_facilities())

    else:
        if ('source' in request.form and 'destination' in request.form and 'tag' in request.form):
            entries = (request.form['source'], request.form['destination'], request.form['tag'])

            # Check to see if the asset exists.
            if (not asset_exists(entries[2])):
                session['message'] = "Asset Not Found: The asset you entered does not exist."
                return redirect(url_for('transfer_req'))

            # Adds the request into the database.
            add_request(session['username'], entries[0], entries[1], entries[2])
            session['message'] = "Your request has been submitted. A facility officer will accept/decline your request."
            return redirect(url_for('message'))

        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Takes the user to a webpage that displays information
on a transfer request a logistics officer had made.
also has a approve and a decline button for the
facility officer to click. Inaccessible by logistic
officers.
"""
@app.route('/approve_req', methods = ['GET', 'POST'])
def approve_req():

    # Loads the approve request page.
    if (request.method == 'GET'):
        session['stamp'] = request.args['ident']
        if (session['role'] != 'Facilities Officer'):
            return redirect(url_for('update_transit'))
        msg = session['message']
        session['message'] = ""

        # Grabs the transfer request information for display.
        res = get_request(session['stamp'])
        user = get_user(res[2])
        src = get_facility(res[6])
        dest = get_facility(res[7])
        asset = get_asset(res[8])
        req = (res[1], asset[1], src[2], dest[2], user[1], time_to_string(res[4]),)
        return render_template('approve_req.html', message = msg, request = req)

    else:
        if ('button' in request.form):

            # User clicked approve, approve the request.
            if (request.form['button'] == 'Approve Request'):
                approve_request(session['stamp'], session['username'])
                session['message'] = "You have approved the request. A logistics officer will submit the load/unload times."
                return redirect(url_for('message'))

            # User clicked decline, delete the request.
            else:
                delete_request(session['stamp'])
                session['message'] = "You have declined the request. The report has been removed from the database."
                return redirect(url_for('message'))

        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))



@app.route('/update_transit', methods = ['GET', 'POST'])
def update_transit():

    # Loads the update transit page.
    if (request.method == 'GET'):
        if (session['role'] != 'Logistics Officer'):
            session['message'] = "Page Restricted: Only logistics officers may access this page."
            return redirect(url_for('error'))
        msg = session['message']
        session['message'] = ""

        # Grabs the transfer request information for display.
        res = get_request(session['stamp'])
        user = get_user(res[2])
        app = get_user(res[3])
        src = get_facility(res[6])
        dest = get_facility(res[7])
        asset = get_asset(res[8])
        req = (res[1], asset[1], src[2], dest[2], user[1], time_to_string(res[4]), app[1], time_to_string(res[5]),)
        return render_template('update_transit.html', message = msg, request = req)

    else:
        if ('loaddate' in request.form and 'loadtime' in request.form and 'unloaddate' in request.form and 'unloadtime' in request.form):
            entries = (request.form['loaddate'], request.form['loadtime'], request.form['unloaddate'], request.form['unloadtime'])

            # Check to see if the entered dates are in a valid format.
            if (not date_valid(entries[0]) or not date_valid(entries[2])):
                session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                return redirect(url_for('update_transit'))

            # Check to see if the entered times are in a valid format.
            if (not time_valid(entries[1]) or not time_valid(entries[3])):
                session['message'] = "Invalid Time: Times must be valid and in the format HH:MM:SS."
                return redirect(url_for('update_transit'))

            # Adds the times into the database.
            update_request(session['stamp'], entries[0] + ' ' + entries[1], entries[2] + ' ' + entries[3])
            session['message'] = "Loading and unloading times have been successfully set."
            return redirect(url_for('message'))
        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Takes the user to a webpage where they can view
a list of transit reports by filtering by the
date, loading, and unloading times.
"""
@app.route('/transfer_report', methods = ['GET', 'POST'])
def transfer_report():

    # Loads the transfer request page.
    if (session.get('report') == None):
        session['report'] = list()
    if (request.method == 'GET'):
        msg = session['message']
        session['message'] = ""
        rprt = session['report']
        session['report'] = list()
        return render_template('transfer_report.html', message = msg, report = rprt)
    else:
        if ('fdate' in request.form and 'ftime' in request.form and 'cdate' in request.form and 'ctime' in request.form):
            entries = (request.form['fdate'], request.form['ftime'], request.form['cdate'], request.form['ctime'])

            # Make sure dates and times are entered together, one may not be left blank
            if (not ((entries[0] != '' and entries[1] != '') or (entries[0] == '' and entries[1] == ''))):
                session['message'] = "Error: You must enter both a date and a time on one of the bounds."
                return redirect(url_for('transfer_report'))
            if (not ((entries[2] != '' and entries[3] != '') or (entries[2] == '' and entries[3] == ''))):
                session['message'] = "Error: You must enter both a date and a time on one of the bounds."
                return redirect(url_for('transfer_report'))

            # Make sure the dates are valid.
            if (entries[0] != ''):
                if (not date_valid(entries[0])):
                    session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                    return redirect(url_for('transfer_report'))
            if (entries[2] != ''):
                if (not date_valid(entries[2])):
                    session['message'] = "Invalid Date: Dates must be valid and in the format MM/DD/YYYY."
                    return redirect(url_for('transfer_report'))

            # Make sure the times are valid.
            if (entries[1] != ''):
                if (not time_valid(entries[1])):
                    session['message'] = "Invalid Time: Times must be valid and in the format HH:MM:SS."
                    return redirect(url_for('transfer_report'))
            if (entries[3] != ''):
                if (not time_valid(entries[3])):
                    session['message'] = "Invalid Time: Times must be valid and in the format HH:MM:SS."
                    return redirect(url_for('transfer_report'))

            # Generates the report, poopulate the table.
            session['report'] = transfers_report(entries[0] + ' ' + entries[1], entries[2] + ' ' + entries[3])
            return redirect(url_for('transfer_report'))
        else:
            session['message'] = "Unknown Error: Something went wrong, return to the dashboard."
            return redirect(url_for('error'))


"""
Send the user to a page containing a message. This message
will be an error message describing the nature of the
redirection (i.e. duplicate entries). User will
be able to redirect back to the dashboard.
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
@app.route('/error', methods = ['GET', 'POST'])
def error():
    # Go to message screen with message.
    return render_template('error.html', message = session['message'])


"""
User has logged out of the system, go to the logout page, link
user back to the login page upon request.
"""
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    # Pop out username from session, go to logout screen.
    session.pop('username', None)
    session['message'] = ""
    return render_template('logout.html')


# Starts and runs the application.
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)


