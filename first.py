#!/usr/bin/python3
from flask import Flask
from frames.department import Department

app = Flask(__name__)

@app.route('/')
def index():
	forest_dept = {
		'name': "Forst Dept",
		'id': '12',
		'link_from': '',
		'link_to': ''
	}

	some = Department(forest_dept)
	some.updateDatato(88888)
	return some.getData("1234") + str(some.getDataFrom())
    #return "Hello, World!"

@app.route('/yeap')
def yeap():
    return "The page two!"


if __name__ == '__main__':
    app.run(debug=True)