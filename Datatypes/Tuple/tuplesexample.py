# Datatype- Tuple
# store multiple items in single variable
# mutable, ordered, indexed, allow duplicates, supports different datatypes
# enclosed in parentheses


tple1 = (1, 2, 3, 4, 5, 6)
print(tple1)
print("type", type(tple1))
tple = (1, 2, 3, 4, 5, 6,"ammu","1.3")  #support multiple datatpye
print(tple)
tple = 1, 2, 3, 4, 5, 6  #comma seperated
print(tple)
tple = [1, 2, 3, 4, 5, 6]
print(tuple(tple))  # convert other datatyes to tuple with keyword tuple
tple = "apple", "mango" ,"apple"  # allow duplicate items
print(tple)
tple=("apple","mango",("banana","orange")) #Nested tuple i possible
print(tple)

# Create Tuple With One Item
# To create a tuple with only one item,
# you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#The tuple() Constructor.
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#tuple support indexing

print(tple[1])  #positive indexing
print(tple[-1]) #last element

#Nested tuple :
nstTuple = ("Amritha", [1,2,3,4], (24,25,26))
print(nstTuple[0])
print(nstTuple[0][1])
print(nstTuple[1][1])





#tuple slicing
print(tple1[1:3])  # return tuple from index 1 to 3 i.e index 1 and 2
print(tple1[::-1])  # reverse
print(tple1[:-5])  # remove last 5 values and returns remaining
print(tple1[::-2]) # returns tuple in reverse order with increment of 2
print(tple1[-3:-1]) #reverse slicing

# tuple can't be update directly as it is immutable datatype.
# So to update a tuple convert to other mutable datatype and update and convert back to tuple
lst=list(tple)
print(lst)
lst[0]="grapes"
print(lst)
print(tuple(lst))

# append a tuple. It can't be append directly as it is immutable datatype
# So to append a tuple convert to other mutable datatype and append and convert back to tuple
lst=list(tple)
lst.append("papaya")
print(lst)
tple = tuple(lst)
print(tple)

#add a tuple . can only concatenate tuple (not "int") to tuple
tple += tple1
print(tple)

#remove a tuple. Can't remove directly. So convert to other mutable datatype and remove

lst=list(tple)
lst.remove("apple")
print(lst)
tple = tuple(lst)
print(tple)

# using del keyword
# doesn't support item deletion
tp= 1,2,3
del(tp) # del keyword remove tuple completely from memory location . generate undefined error on print tp

#Unpacking tuple:
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# method 1
fruits = ("orange", "apple","banana")
(orange,red,yellow) = fruits
print(orange)
print(red)
print(yellow)

#method2 Using Asterik
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("orange", "apple", "banana", "grapes", "cherry")
(orange,red,*yellow) = fruits
print(orange)
print(red)
print(yellow)

#If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values
# left matches the number of variables left.

fruits = ("orange", "apple", "banana", "grapes", "cherry")
(orange,*tropic,yellow) = fruits
print()
print(orange)
print(tropic)
print(yellow)

#all()
tp=()
tp1=(1,2)
tp2 = (0, False, False)
tp3 = (True, True, True)
tp4 = (1, True, True)
tp5 = (0, True, True)
print(all(tp))
print(all(tp1))
print(all(tp2))
print(all(tp3))
print(all(tp4))
print(all(tp5))

# enumerate


















