str1= "Hello"
str2= "World"
str3 = 4
str4 = '4'
print(str1 + str2)
print(str1 + ' '+str2)
print(str1 + ' '+str4)
# cannot concatenate number and a string. otherwise need to convert num to string using 'str' and then concatenate
print(str1 + str(str3))

print('length of str1 ' , len(str1))

#Loops through string

# 1. using while loop
print("\nwhile loop")
fruit= 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter,index)
    index+=1

# 2. using for loop
print("\nfor loop")
fruit= 'orange'
for x in fruit:
    print(x)

#find() method
fruit= 'banana'
print(fruit.find('na'))
print(fruit.find('aa'))

#replace() method

str1 = "Helooo Bob"
print(str1.replace('Bob','Jane'))
print(str1.replace('o','X'))
b=str1[:5].replace('o','j')
print(b)
print(str1.replace('o','X',1)) # 1 is the count for replacing
