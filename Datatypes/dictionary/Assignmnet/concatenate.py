# concatenate two dictionaries

# using update() method
dict1 = {"Name": "Amal", "Age": 25, "course": "Java"}
dict2 = {"state": "kerala", " Gender": "Male"}
dict1.update(dict2)
print(dict1)

# using merge(|) method
dict1 = {"Name": "Amal", "Age": 25, "course": "Java"}
dict2 = {"state": "kerala", " Gender": "Male"}
dict3 = dict1 | dict2
print(dict3)

# Using ** operator
dict4 = {**dict1, **dict2}
print(dict4)




