from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rest/activate_user')
def activate_user():
	"""FIXME"""
	return

@app.route('/rest/add_asset')
def add_asset():
        """FIXME"""
	return

@app.route('/rest/add_productions')
def add_productions():
	"""FIXME"""
	return

@app.route('/rest/list_products')
def list_products():
        """FIXME"""
	return

@app.route('/rest/lost_key')
def lost_key():
        """FIXME"""
	return

@app.route('/rest/suspend_user')
def suspend_user():
        """FIXME"""
	return
	
