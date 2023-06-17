#List
"""
Features

- sequence of values called items/elements
- allow multiple data types
- allow duplicate elements
- mutable
- ordered
- indexed
- enclosed in [] separated by comma

"""
list1 = [1,2,3,4,5]
print(list1)
print(list1[0])
print(list1[4])

#listslicing
print(list1[2:5])
print(list[2:5])
print("slicing",list[:-1])

#List allow different datatypes as elements
list2=[1,2,3,4,5,'akshaya','jane']
print(list2)

#Nested List
list3 = ["welcome", [8,4,6], "Hi"]
print(list3[0])
print(list3[1])
print(list3[0][0])
print(list3[1][0])
print(list3[1][1])
print(list3[1][1:3])
print(list3[2][0])
print(list3[2])
print(list3[2][0:2])

#Positive and Negative indexing
print(list1[1])
print(list1[-1])

#append() - add element to the list at last position
list2.append('amritha')  #will exactly take only one argument
print(list2)
list2.append('ammu')
print(list2)
list2.append(list1)
print(list2)

list2.remove("ammu")
print(list2)

list2.insert(3,"ammu")
print(list2)
lst = ['a',['bb','cc'],'d']
lst[1].insert(1,'ss')
print(lst)

# .extend()- merge two list
list2.extend(list3) # extend() method take only one argument
print(list2)

# .pop() Removes and returns an element at the given index
list4=[50,60,70]
print(list4.pop(1))
print(list4)

#clear() removes all items from list
list4.clear()
print(list4)

#index() : return index of first matched string
lst=["ammu","laks","ammu"]
#lst.index(m)
print(lst.index("laks"))
str1 = "hello world"
print(str1.index("o"))

# count() returns count of items passed as argument
print(lst.count("ammu"))
#lst=[1,2,3,4,1,2]
#print(list.count(1)) #'count' for 'list' objects doesn't apply to a 'int' object

# sort() - sort item in a list in ascending order
lst.sort()
print(lst)


# reverse() - reverse order of the item in the list
lst.reverse()
print(lst)

#copy() returns shalow copy of the list
lst1=lst.copy()
print(lst1)



