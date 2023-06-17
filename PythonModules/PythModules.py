"""

A file containing a set of functions you want to include in your application.
"""

# import calcu
# from calcu import add
#
# print(add(4,6))


"""
import os >> file handling
os.mkdir()
"""
# import os
# #os.mkdir("E:\pythonModule1")
# #os.rmdir("E:\pythonModule")
# os.chdir("E:\AVILinx")
# print(os.getcwd()) # will not take any arguments


"""
JSON Module  JAVASCRipt object notation

"""

import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)