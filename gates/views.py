'''Setup for app.'''

from flask import render_template, url_for, redirect
from functools import wraps

from gates import app

def detectLogin(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if loggedIn():
			return func(args, kwargs)
		return redirect(url_for('login'))
	return wrapper

@app.route('/')
@detectLogin
def home():
	return render_template('orders.html', title='My Orders')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')


def loggedIn():
	return False