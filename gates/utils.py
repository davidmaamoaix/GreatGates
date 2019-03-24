'''Useful utils.'''

from requests import post
from bs4 import BeautifulSoup

def login(username: str, password: str) -> list:
	'''
	Logs into powerschool with the given account.

	Parameters:
		username: the username of the user
		password: the password of the user

	Returns: (flag: int, stuId: str, name: str)
		flag:
			0: Success
			1: Incorrect data
			2: Internal error
		name: student name
	'''
	url = 'https://powerschool.ykpaoschool.cn/guardian/home.html'
	form = {
		'account': username,
		'ldappassword': password,
		'pw': 'derp'
	}

	try:
		response = post(url, data=form, timeout=7)
		bsObj = BeautifulSoup(response.text, 'html.parser')
		name = bsObj.select('#userName > span')
		if len(name) == 0:
			return 1, None
		name = name[0].get_text().strip()
		return 0, name
	except Exception as e:
		return 2, str(e)
