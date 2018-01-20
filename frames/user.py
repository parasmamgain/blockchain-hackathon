#!/usr/bin/python3

class User(object):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__()
        # self.arg = arg
        self.id = arg['id']
        self.is_logged_in = arg['is_logged_in']
        self.requests = arg['requests']
