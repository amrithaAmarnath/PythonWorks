#count of the letters from the string.
# here count is count of each char in a string
#str1 = "Luminar Python"
# str1 = str1.replace(" ","")
# str1 = str1.lower()

dict1 = {}
# for i in str1:
#     dict1[i] = str1.count(i)
#
# print(dict1)

# here count means index
str1 = "Luminar"
for index in range(1, len(str1)+1):
    dict1.setdefault(index, str1[index-1])
   # print(str1[index - 1])
print(dict1)
