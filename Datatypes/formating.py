#string formatting
# to make more readable

"""
Python f-string
- new Python syntax to do string formatting
- to give msg more readable
-faster
- use {}
"""
#eg 1
name = "Peter"
age = 23

print('%s is %d years old' %(name,age))

# Another 2 methods. Below methods are used in commercial level
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')

# eg 2
bags = 3
apples_in_bag = 12
print(f'There are total of {bags * apples_in_bag} apples')

#eg 3
val1 = 4
val2 = 5
val3= val1+ val2
print(f'The sum is {val1 + val2}')
print("The sum is {}".format(val3))
print("The sum is {}".format(val1 + val2))



