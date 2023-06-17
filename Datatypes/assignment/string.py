str1="india is my country"

#1. Check if each word begins with a capital letter

print("1.Does each word begins with a capital letter ? ",str1.istitle())

#2. Check if a string contain a specific substring

subString="my"
print("2.Does the string contain the substring '",subString,"' ? ", subString in str1)

#3.Find the index of the first occurrence of a substring in a string
print("3. Index of the first occurrence of a substring '",subString,"' ? ", str1.find(subString))

#4.	Count the total number of characters in a string
print("4. Total number of characters in string = ",len(str1))

#5. Count the number of a specific character in a string
print("5. number of a specific character 'i' : ",str1.count('i'))

#6. Capitalize the first character of a string
print("6. Capitalize the first character : ",str1.capitalize() )

#7.	Check if a string contains only numbers
print("7. Does the string has only number? ",str1.isnumeric())

