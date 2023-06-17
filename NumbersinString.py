#extract numbers in a string using List compreshion
str1="The rooms 65 and 47 are vacant"
n=[x for x in str1.split(" ") if x.isdigit()]
print(n)
