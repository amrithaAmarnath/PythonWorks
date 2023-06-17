"""
List comprehension offers a shorter syntax to create a new list based on
the values of an existing list.

Without list comprehension you will have to write a for statement with a conditional test inside:



Example:

Based on a list of fruits, you want a new list, containing only the fruits
 with the letter "a" in the name.

"""
#Nomal method
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
newlist = [x for x in fruits if "a" in x]
print(newlist)
"""
The Syntax
newlist = [expression for item in iterable if condition == True]

Condition:
The condition is like a filter that only accepts the items that valuate 
to True.

Iterable:
The iterable can be any iterable object, like a list, tuple, set etc.
Can use the range() function to create an iterable:

"""

# Accept only numbers lower than 5
numlist=[x for x in range(5)]
print(numlist)

"""
Expression:
The expression is the current item in the iteration, but it is also the outcome,
 which you can manipulate before it ends up like a list item in the new list:
"""
newlist = [x.upper() for x in fruits if "a" in x]
print(newlist)

#The expression can also contain conditions, not like a filter, but as a
# way to manipulate the outcome:

newlist = [x if x != "banana" else "orange" for x in fruits] #Return the item if it is not banana, if it is banana return orange"
print(newlist)
print([x for x in "hello world"])

#print numbers divisible by 2 and 5 for the range less than 100
newlist=[x for x in range(100) if x % 2 == 0 if x % 5 == 0 ]
print(newlist)

#print prime numbers between 2,21
newlist=[x for x in range(2,21) if all(x % y !=0 for y in range(2,x//2+1)) ]
print(newlist)

h_letters = [letter for letter in 'human']
print(h_letters)

#even
even=[x for x in range(101) if x % 2 ==0 ]
print(even)

#even
even=[x for x in range(101) if x % 2 ==0 ]
print(even)

#odd
odd=[x for x in range(101) if x % 2 !=0 ]
print(odd)

#sum of n natural numbers 1 to 10
s=0
sums= sum([x for x in range(1,11)])
print(sums)
# sums= sum([x for x in range(1,int(input("enter limit"))+1)])
# with equation of sum of n natural munbers n(n+1)/2
sums=0
sums= [x*(x+1)/2 for x in range(1,int(input("enter limit"))+1)]

print(sums)





