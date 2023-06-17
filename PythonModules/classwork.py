"""

wapp to generate a random color hex, a random alphabetical string,
random value between two integers and random multiple of 7between 0 and 70
Hint: Use random.randint()

"""
import string
import random
print(dir(random))
print(random.randint(0,0xFFF))

print(str(hex(random.randint(0,0xFFF))))
hexnum=str(hex(random.randint(0,16777215)))
hexnum ='#'+ hexnum[2:]
print(hexnum)
#print("%06x" % random.randint(0,0xFFF))

# str1=random.choice(string.ascii_letters)
# print(str1)

max_length = 100
str1 = ""
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_lowercase)
print(str1)

print(random.randint(1,25))
print(random.randint(1,10)*7)




