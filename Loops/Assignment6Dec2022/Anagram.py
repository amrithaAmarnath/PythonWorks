#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

str1 = input("enter first string")
str2 = input("enter second string")
anagram = 'false'
str1="".join(str1.split())
str2="".join(str2.split())
str1 = str1.lower()
str2 = str2.lower()

list1 = list(str1)
list2 = list(str2)
list1.sort()
list2.sort()
# print(list1)
# print(list2)

if list1 == list2:
    anagram = 'true'
else:
    anagram = 'false'
print(f' anagram = {anagram}')


# print(str1)
# print(str2)
# if len(str1) == len(str2):
#     for i in str1:
#         if(i in str2 and str1.count(i) == str2.count(i)):
#             anagram = 'true'
#         else:
#             anagram = 'false'
#             break
# else:
#     anagram = 'false'
#
# print(f' anagram = {anagram}')