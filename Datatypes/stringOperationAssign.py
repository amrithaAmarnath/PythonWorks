#String operations
# 1.string indexing
str1 = "India is my country" #input("enter string")
print("character in index 0 :",str1[0])
print("character in index 2 :",str1[2])
print("last index character :" , str1[-1])
print("second last index character :" ,str1[-2])

# 2.string slicing
print("Reverse string :",str1[::-1])
print("string without last letter :",str1[:-1])
print("characters from position 2 to position 5 : ", str1[2:5])
print("characters from position 5 to position 1, \n"
      " starting the count from the end of the string is ", str1[-5:-2])
print("reverse string with alternate letters",str1[::-2])
print("first word", str1[0:5])
print("reverse first word ", str1[-14:-20:-1])
print("second word",str1[6:8])
print("reverse the second word : ", str1[-11:-14:-1])

# 3. String Methods
str2=str1.upper();
print("uppercase : ", str1.upper())
print("Lowercase:", str2.lower())
print("Capitalize first letter of each word", str1.title())
print("Capitalize first letter:", str1.capitalize())
print("swapcase:", str1.swapcase())
print("check if string has only alphabets without space",str1.isalpha())
print("check if lowercase",str1.islower())
print("check if uppercase",str2.isupper())
