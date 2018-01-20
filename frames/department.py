#!/usr/bin/python3

class Department(object):
	"""docstring for Department"""
	def __init__(self, arg=None):
		super(Department, self).__init__()
		self.name = arg['name']
		self.id = arg['id']
		self.link_from = arg['dept_before']
		self.link_to = arg['dept_after']

	def getData(self, data):
		return "Some statement" + data

	def updateDatato(self, update):
		self.y = update or self.y

	def getDataFrom(self):
		return self.y