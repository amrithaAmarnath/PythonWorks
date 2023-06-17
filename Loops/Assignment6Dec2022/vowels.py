# check for a,e,i,o,u and A,E,I,O,U
vowels = ['a','e','i','o','u','A','E','I','O','U']
str1 = input("enter a string")
for i in str1:
    if i in vowels:
        print(f' {i} is vowel')
    else:
        print(f' {i} is consonant')