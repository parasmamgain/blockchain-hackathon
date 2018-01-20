#!/usr/bin/python3

class Comments(object):
    """docstring for Comments."""
    def __init__(self, arg):
        super(Comments, self).__init__()
        # self.arg = arg
        self.id = arg["id"]
        self.data = arg["data"]
        self.user_id = arg["user"]
        self.request_id = arg["request_id"]


#TODO: include this class in the DepartmentProcess class
