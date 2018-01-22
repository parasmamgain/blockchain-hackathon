#!/usr/bin/python3

from frames.comments import Comments

class DepartmentProcess(Department, Process):
    """docstring for DepartmentProcess."""
    def __init__(self, arg):
        super(DepartmentProcess, self).__init__()
        self.from_department = arg['from_department']
        self.to_department = arg['to_department']
        self.status = arg["status"]
        self.rules = arg["rules"]


#TODO:
# 1. status should be one of four
# 2. rules is a seperate class, also how do you define it?
# 3. integrate comments  
#
