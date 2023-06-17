
#14.	Remove whitespace from the left, right or both sides of a string
str3=" my country "
print('remove spaces from  left :', str3.lstrip())
print('remove spaces from right :', str3.rstrip())
print('remove spaces from sides :', str3.strip())

#15.	What does it mean for strings to be immutable in Python?
a=""" \n15. In python, the string data types are immutable, which means, a string value cannot be updated.
     For example: if t="mango" , we cannot assign t[0]="M". This leads to an error.
"""
print(a)