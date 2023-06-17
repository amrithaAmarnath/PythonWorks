str1 = input("enter string ")
str1 = str1.lower()
c=[]
for i in str1:
    if str1.count(i) == 1:
        c.append(i)

print(f'non repeating characters {c}')
