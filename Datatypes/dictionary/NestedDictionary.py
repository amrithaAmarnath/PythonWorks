dict1 = {"employee1":{"Name":"Amritha", "Age":30, "course":"Python"},
         "employee2":{"Name": "Athulya", "Age":27, "course":"Mern"}}
print(dict1)
print(type(dict1))
print(dict1["employee1"]["Name"])
print(dict1["employee2"]["Age"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get("employee1"))
#update
dict1["employee1"]["Age"] = 29
print(dict1["employee1"] )
dict1["employee1"].update({"state":"kerala"})
print(dict1["employee1"] )

# Add
dict2 = { "Name":"veda", "Age":20, "course":"Python"}
dict3= {"Name":"Ammu", "Age":25, "course":"Mern"}
dict1["employee3"]=dict2
dict1.update({"employee4":dict3})
print(dict1)

#Remove items
dict1.pop("employee3")
print(dict1)
dict1.popitem() #remove last item
print(dict1)

#Loop
for i in dict1:
    print(i)

for i in dict1.values():
    print(i)

for i in dict1.values():
    print(i["Name"])

for i in dict1.items():
    print(i)

#copy
c= dict2.copy()
print("c = ",c)






