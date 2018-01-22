#!/usr/bin/python3

class Request(object):
    """docstring for Request."""
    def __init__(self, arg):
        super(Request, self).__init__()
        # self.arg = arg
        self.id = arg["id"]
        self.timestamp = arg["timestamp"]
        self.status = arg["status"]
        self.category = arg["category"]


#TODO:
# 1. Are categories valid/necessary? How do we implement them?
# 2. Status should be one of [""Approved", "Rejected", "In Progress", "Not yet started" "]
# 3. Timestamp should be automatically given during creation of request
