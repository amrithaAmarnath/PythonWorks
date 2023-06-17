# map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
#convert the map into a list, for readability:
print(list(x))

def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))




def addition(n):
  return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

