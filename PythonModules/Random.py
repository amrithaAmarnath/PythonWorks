#pseudo-random generator
import random
print(dir(random))

print(random.random()) #
print(random.randint(1,100)) # return random integer number between 1 to 100
print(random.randrange(1,10,2))
print(random.choice("amritha"))
print(random.choice([50,20,6,17,30,5]))
print(random.choice((50,20,6,17,30,5)))
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)
num=[50,20,6,17,30,5]
random.shuffle(num)
print(num)