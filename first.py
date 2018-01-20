#!/usr/bin/python3
from flask import Flask
from flask import *
from frames.user import User
from frames.request import Request


app = Flask(__name__)

# , methods=['GET', 'POST']
@app.route('/')
def index():
	forest_dept = {
		'name': "Forst Dept",
		'id': '12',
		'link_from': '',
		'link_to': ''
	}
	# processes = Department(forest_dept)
	# processes.updateDatato(88888)
	# return some.getData("1234") + str(some.getDataFrom())
	return render_template('index.html')

@app.route('/dashboard')
def show_dashboard():
	user1 = {
		"id": "001",
		"is_logged_in": False,
		"requests": ["01", "02"]
	}
	req1 = {
	"id": "01",
	"timestamp":"t62u3ygq",
	"status":"In Queue",
	"category": "Felling"
	}
	req2 = {
	"id": "02",
	"timestamp":"t62u3sdygq",
	"status":"In Process",
	"category": "Transit"
	}
	user = User(user1)
	user.is_logged_in = True
	requests = user.requests

	return render_template('dashboard.html', requests=requests)

@app.route('/new-felling-request')
def new_felling_request():
	return render_template('new_felling_request.html')

if __name__ == '__main__':
    app.run(debug=True)




# on start, spawn dashboard.
