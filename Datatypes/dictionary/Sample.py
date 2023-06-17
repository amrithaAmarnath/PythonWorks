# data store in key -value pair
# keyword 'dict'
#muttable, ordered,indexed, do not allow duplicates.
#The values in dictionary items can be of any data type

dict1 = {"Name":"Amritha","Age":12,"course":"Python"}
print(type(dict1))
print(dict1["Name"]) # to access value of a key in dictionary
print(dict1.get("Name")) # to access value of a key in dictionary using get() method
print(dict1.keys()) # to get keys in dictionary using key() method
print(dict1.values()) # to get values in dictionary using value() method
print(dict1.items()) # to get key-value pairs in dictionary as tuples
print(len(dict1)) # length of dictionary

#change values of a key in dictionary
dict2 = {"Name":"Amritha","Age":12,"course":"Python"}
dict2["Age"] = 25
print(dict2)

#update() method to change values
dict2.update({"Name":"Lakshmi","Age":30})
print(dict2)

#Add Dictionary Items
dict2["state"] = "kerala"
print(dict2)
# Add multiple items using update() method
dict2.update({"occupation":"software engineer" , "company":"AmritaTech"})
print(dict2)

#Remove Dictionary items
# - pop() method
dict2.pop("state")
print(dict2)
# - popitem()
dict2.popitem()
print(dict2)
# del keyword
del dict2["course"]
print(dict2)
#del can also delete the dictionary completely from memory space .
# So print() creates undefined error
dist3={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dist3

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# copy() method
d={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
c=d.copy()
print("c = ",c)

#Loop in dictionary
for i in dict1:
    print(i) # print keys only


for i in dict1.keys(): # print keys only
    print(i)

for i in dict1.values(): # print values only
    print(i)

for i in dict1.items():
    print(i) # print key value pair as tuples




