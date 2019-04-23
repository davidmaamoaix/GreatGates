'''Setup for app.'''

from flask import render_template, url_for, redirect, session, request, flash
from functools import wraps

import re
from gates import app
import gates.constants as constants
import gates.data as data
import gates.utils as utils
from gates.recorder import current as recorder

def detectLogin(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if loggedIn():
			return func(*args, **kwargs)
		return redirect(url_for('login'))
	return wrapper

@app.route('/')
@detectLogin
def home():
	orderData = data.getOrders(session['name'])
	return render_template(
		'orders.html',
		title='My Orders',
		pending=orderData[0],
		finished=orderData[1]
	)

@app.route('/login', methods=["GET", "POST"])
def login():
	if loggedIn():
		return redirect(url_for('home'))

	if request.method == 'GET':
		return render_template('login.html', title='Login')

	form = request.form
	response = utils.login(form['username'], form['password'])

	if response[0] == 0:

		# Success.
		session['logged_in'] = True
		session['name'] = re.sub(r' \([^)]*\) ', ' ', response[1])
		session['username'] = form['username']

	elif response[0] == 1:

		# Incorrect data.
		flash('Incorrect username or password')

	else:

		# Internal error.
		flash('Server is busy')

	return redirect(url_for('home'))

@app.route('/buy')
@detectLogin
def buy():
	return render_template(
		'buy.html',
		title='Buy',
		items=constants.ITEMS
	)

@app.route('/submit', methods=["GET", "POST"])
@detectLogin
def submit():
	#if request.method == 'GET':
		#return redirect(url_for('home'))

	return render_template('success.html', title='Order Completed')

@app.route('/logout')
@detectLogin
def logout():
	del session['logged_in']
	del session['name']
	del session['username']
	return redirect(url_for('login'))

def loggedIn():
	return session.get('logged_in')