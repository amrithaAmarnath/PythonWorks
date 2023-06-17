#import string
"""
week 3 Assignments

1.	Remove empty strings from a list of strings
Str1 = [“John”, “ ”,“Jack”,”Emma”,” ”,”Jins”,”Lina”]
o/p: Str1 = [“John”,“Jack”,”Emma”,”Jins”,”Lina”]

"""
# Str1 = ["John", " ", "Jack", "Emma", " ", "Jins", "Lina"]
# # 1st method
# while " " in Str1:
#      Str1.remove(" ") #The remove() method removes the specified item.
# print(Str1)


# 2nd method
# newList= ' '.join(Str1).split()
# print(newList)

# 3rd method >> Remove None values from list using Filter method
# Str1 = ["John", "", "Jack", "Emma", "", "Jins", "Lina"]
# newList=list(filter( None, Str1))
# print(newList)


"""
2.	Write a python code to remove all the repeating letters  
    from a each words of a given sentence.
Eg:
   			i/p:Let’s google the pineapple
 			o/p:Let’s gole the pineal

"""
# inp = "Let’s google the pineapple"
# ip = []
#
# print(inp.split())
# for i in inp.split():
#     print(i)
#     print(dict.fromkeys(i))
#     res="".join(dict.fromkeys(i)) # The fromkeys() method returns a dictionary with the specified keys and the specified value.
#     # print(res)
#     ip.append(res)
#     result = " ".join(ip)
# print(result)

#another method

inp = "Let’s google the pineapple"
ip = []
for i in inp.split():
    l=""
    for j in i:
        if j in l:
            continue
        else:
            l= l+j
    ip.append(l)
ip = " ".join(ip)
print(ip)


"""
3.	Replace each special symbol with # in the following string
  str1 = '/*Jon is @developer & musician!!'
 o/p:    ##Jon is #developer # musician##

 """
#str1 = '/*Jon is @developer & musician!!'
# chars=['/','*','&','!','@']
# for i in str1:
#     if i in chars:
#       str1=str1.replace(i,'#')
# print(str1)

# another method need to check

# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)
#
# # Replace punctuations with #
# replace_char = '#'
# print(string.punctuation)
# # string.punctuation to get the list of all special symbols
# for char in string.punctuation:
#     str1 = str1.replace(char, replace_char)

# print("The strings after replacement : ", str1)

"""
4.	Reverse a list in Python
list1 = [100, 200, 300, 400, 500]

"""
#list1 = [100, 200, 300, 400, 500]
# print("reverse list = ",list1[::-1])
#list1.reverse()
# print(list1)

"""
5.	Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
Expected Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

"""

#list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# print(list1)
# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)


