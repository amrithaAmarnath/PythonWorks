str1="Made in India"

#8.	Split a string on a specific character
print("8. split on a specific character : ", str1.split("i"))

#9.	Reverse the string “hello world”
str2="hello world"
print("9. Reverse string 'hello world ' : ", str2[::-1])

#10. Join a list of strings into a single string, delimited by hyphens
st=str1.split() # st="-".join([str1,str2])
print("10. Join a list of strings into a single string, delimited by hyphens:  ",'-'.join(st))

#11.	Give an example of string slicing
print("11. Eg of string slicing: ", str1[3:7]) #str1[:0:-2]

#12.	Convert an integer to a string
a = 24
print("12. convert integer 24 to string > " , type(str(24)))  # "{}".format(a)

#13.	Replace all instances of a substring in a string
print("13. replace India with USA: ", str1.replace('India','USA'))
