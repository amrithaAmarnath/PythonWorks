# 1. Read a string and find the number of unique characters in it.

data = "cranes varsity bangalore"
unique = set(data)
print("unique characters ",unique)

# to find repeated characters
data = list(data)

for elem in unique:
   data.remove(elem)
print("Repeated characters",set(data))

#2.

studentlist = {'dhanish' , 'amritha', "ammu", 'athulya','uma','John','veda','roy'}

placedstudent = ['veda', 'ammu', 'amritha']

nonplacedstudent = set(studentlist) - set(placedstudent)

print(nonplacedstudent)

#3.



