#all()
tp=()
tp1=(1,2)
tp2 = (0, False, False)
tp3 = (True, True, True)
tp4 = (1, True, True)
tp5 = (0, True, True)
print("all() of empty tuple is  ",all(tp))
print(f'all() of {tp1} is  {all(tp1)}')
print(all(tp2))
print(all(tp3))
print(all(tp4))
print(all(tp5))


# any()  >> Return True if any element of the tuple is true. If the tuple is empty, return False.
print("any(tp5)",any(tp5))

# enumerate() >> Return an enumerate object. It contains the index and value of all the items of
# tuple

t= 1,50,25,10
print(f' enumerate object of {t} is  {enumerate(t)}')
e= enumerate(t)
print(f' index,value pair in enumerate object is {tuple(e)}')

letters = [('a','A'),('b','B')]
for i,letters in enumerate(letters):
    print(i,letters)
    print(f' Letter #{i} is {letters[0]}/{letters[1]}')
    print(" Letter #%d is %s/%s" %(i,letters[0],letters[1]))
#list
names = ['Mukesh', ' Roni', 'Chari']
ages = [24, 50, 18]
for i, (name,age) in enumerate(zip(names, ages)):
    print(i, name, age)


#len()
print("length of tp3= ",len(tp3))

# max()  >> Return the largest item in the tuple.
t= 1,50,25,10
print(f'max of {t} is {max(t)}')

# min()  >> Return the smallest item in the tuple.
t= 1,50,25,10
print(f'min of {t} is {min(t)}')

#sorted() >> Take elements in the tuple and return a new sorted list (does not sort the tuple  itself).
print(f'sorted {t} is {sorted(t)}')

# sum() >> Retrun the sum of all elements in the tuple.
print(f'sum of tuple {t} = {sum(t)}')

# tuple() >> Convert an iterable (list, string, set, dictionary) to a tuple.
lst = [1,2,3,5,6]
print(tuple(lst))

#tuple of dictionary
dct = {"a":1,"b":2}
print(tuple(dct))

#tuple of string
st = "Luminar"
print(tuple(st))

# tuple of tuple
print(tuple(t))

# tuple of set.
s = {"apple", "banana", "cherry"}
print(tuple(s))
print("*********map()*********")
#map() method
#List

l =['sat','bat','cat','mat']
test = list(map(tuple,l))  # map()can listify the list of string individualyy
print(test)

#tuple
test = tuple(map(tuple,l))
print(test)

#set
test = set(map(tuple,l)) # set(map(set,l))  is not possible
print(test)



