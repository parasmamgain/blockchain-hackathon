#!/usr/bin/python3

class Process(object):
    """docstring for Process."""
    def __init__(self, arg):
        super(Process, self).__init__()
        # self.arg = arg
        self.id = arg[id]
        self.name = arg[name]
        self.departments = arg[departments]

#TODO:
# 1. departments should be a part of the existing list of department objects only
# 2. 
