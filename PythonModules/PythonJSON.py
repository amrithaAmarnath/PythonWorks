"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.

SON in Python
Python has a built-in package called json, which can be used to work with JSON data.
"""

import json

"""
1. Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
Result: Python Dictionary
"""
# some JSON:
x='{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y=json.loads(x)
#result Python Dictionary

print(y)
print(y["age"])


"""
2. Convert from Python to JSON

Python object can convert into a JSON string by using the json.dumps() method.
"""
#Python Dictionary
z={ "name":"John", "age":30, "city":"New York"}
s=json.dumps(z)
print(s)