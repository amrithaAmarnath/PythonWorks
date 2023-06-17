#1. Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'
str2 = str1.replace('/','#').replace('*','#').replace('@','#').replace('&','#').replace('!','#')
print(str1)
print("1.replace /*@&! with # : ",str2)
#chars=[/*&!@]

#2. Append new string in the middle of a given string s3 = "LumiPythoninar"
s1 = "Luminar"
s2 = "Python"
#print("s1 is {s1}")
lengthOfs1=len(s1)
middle_index=lengthOfs1 // 2
print(middle_index)
#lengthOfs2=len(s2)
s3 = s1[0:(middle_index+1)]
print(s3)
s4 = s1[middle_index:lengthOfs1]
print(s4)
newString=s3+s2+s4
print(newString)
