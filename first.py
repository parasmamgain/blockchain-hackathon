#!/usr/bin/python3
from flask import Flask
from flask import *
from frames.user import User
from frames.request import Request
import json

app = Flask(__name__)

# , methods=['GET', 'POST']
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard')
def show_dashboard():

	requests_json = open('data/requests.json')
	request_str = requests_json.read()
	requests = json.loads(request_str)

	req_type = request.args.get('type')
	if not req_type == None:
		requests = [r for r in requests if r['type'] == req_type]

	return render_template('dashboard.html', requests=requests)

@app.route('/new-felling-request')
def new_felling_request():
	return render_template('new_felling_request.html')

@app.route('/request-info')
def request_info():

	trees_json = open('data/trees.json')
	trees_str = trees_json.read()
	trees = json.loads(trees_str)

	requests_json = open('data/requests.json')
	request_str = requests_json.read()
	requests = json.loads(request_str)

	req_id = request.args.get('_id')
	requests = [r for r in requests if r['_id'] == req_id]

	return render_template('request_info.html', trees=trees, requests = requests )




if __name__ == '__main__':
    app.run(debug=True)
