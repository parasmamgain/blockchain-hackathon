#!/usr/bin/python3

class Department(object):
	"""docstring for Department"""
	def __init__(self, arg):
		super(Department, self).__init__()
		self.name = arg['name']
		self.id = arg['id']
		self.link_from = arg['link_from']
		self.link_to = arg['link_to']

	def getData(self, data):
		return "Some statement" + data

	def updateDatato(self, update):
		self.y = update or self.y

	def getDataFrom(self):
		return self.y