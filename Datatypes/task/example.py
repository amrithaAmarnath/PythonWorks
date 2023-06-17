"""
1. Write a program to get a string from a given string, where all the occurrences
of its first char have been changed to '$', except the first char itself.
sample i/p: 'restart'
o/p: 'resta$t'

2. WAP for python function that takes a list of words and returns the
 length of the longest one.

"""
# Q1
# str1 = 'restart'
# str2 = str1[0]
# str1 = str1.lower()
# for i in range(1, len(str1)):
#     if str1[i] == str1[0]:
#         str2 = str2 + "$"
#         print(str2)
#     else:
#         str2 = str2+str1[i]
#         print(str2)
# print(str2)


# Using replace method
# str1 = 'restart'
# ch = str1[0]
# length=len(str1)
# str1 = str1.replace(ch,"$")
# str3 = ch + str1[1:]
# print(str3)


#Q2
l=[]
lst=list(input("enter space separated words").split())
for i in lst:
  #  ln = len(i)

    l.append(len(i))

m=max(l)

# m=max(lst)  #
print(f'length of the longest word is {m}')


#
# #using function
# def longest(ls):
#     return len(max(ls))
# lmax = longest(lst)
# print(lmax)



