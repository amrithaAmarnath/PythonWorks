#Assignment

#1. Sum of all items in as list.
My_list = [1,2,3,4,5]
sum = 0;
for x in My_list:
    sum = sum + x
print(f'1.sum = {sum}')

#2. Write a Python program to get the largest number from list
List1 = [1, 2, -8, 0]
largest = 0
for x in List1:
    if x > largest:
        largest = x

print(f'2. Largest number is {largest}')

List2=[1, 2, -8, 0]
List2.sort()
l=len(List2)
lg=List2[l-1]
print(f'2. Largest number is {lg}')


#3. Python program to convert a list of characters into a string
s= ['p', 'y', 't', 'h', 'o', 'n']
st1="".join(s)
print(f'3.{st1} ')

#4. Multiply all items in a list
My_list = [1,2,3,4,5]
product = 1;
for x in My_list:
    product = product * x
print(f'4.product = {product}')
