"""  triple
1. Number
2. Sequence - String (immutable, ordered), List, Tuple
3.Boolean
4. Dictionary
5. set - undordered

"""
#Number

x=2;
print(x);
y = 5.1
print(type(y))

#String => immutable
str1= "Hello world"
age="14"
print(type(str1))
print(type(age))
#string indexing
print(str1[0])
print(str1[2]) #forward indexing
print(str1[-1]) #rever or negative indexing
#string slicing
print(str1[7:10])
print(str1[:-1]) #negative slicing
print(str1[::-1])#reverse slicing . Completly reverse the string
print(str1[::-2])#reverse string with alternate letters
print(str1)
print(str1[::-3])# reverse string with every 3rd letters
print(str1[::-4])
print(str1[-3:-1])
print(str1[-1:-6:-1]) # reverse world > last -1 represent reverse
print(str1[-7:-12:-1]) # reverse hello
print(str1.upper())
str2=str1.upper();
print(str2.lower())
print(str1.capitalize())
print(str1.swapcase())
print(str2.title())
print(str1.isalpha()) # only alphabets without space or numbers
print(str1.islower())
print(str2.isupper())


#List
list1 = [1,2,3]
print(list1)
print(type(list1))

#Dictionary
dict = {"name":"amritha", "age":20}
print(dict)
print(type(dict))

#Tuple

a= ('ammu', 'priya');
print(a)
print(type(a))

#Set
a={1,2,3}
print(a)
print(type(a))




