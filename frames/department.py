#!/usr/bin/python3

class Department(object):
	"""docstring for Department"""
	def __init__(self, arg):
		super(Department, self).__init__()
		self.name = arg['name']
		self.id = arg['id']
		
	# def view_request(self):
	# 	return "Some statement"
    #
	# # def assign_request_status(self, request, status):
	# 	# self.request = status or self.y
    #
	# def assign_request_msg(self, msg):
	# 	self.y = status_msg or self.y
    #
	# def getDataFrom(self):
	# 	return self.y
    #
	# def rules(self):
	# 	return self
	# 	# rules, approved status, approved message
