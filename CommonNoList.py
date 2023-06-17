"""

1.	Write a program to separate negative and positive numbers from a given list ?(accept input from the user.)
2.	 Write a python program to find the sum of all numbers in a list
3.	 Write a python program to find largest number in a given list with out using max()
4.	 Write a python program to find the common numbers from two lists
5.	 Write a python program to print all even numbers from a given list
6.	 Write a python program to create a list of even numbers and another list of odd numbers from a given list
7.	 Write a python program to remove repeated elements from a given list without using built-in methods
8. ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
Write a python program to print website suffixes (com , org , net ,in) from this list.
9.Reverse a given tuple .
10.Check if all items in tuple are same10.Check if all items in the tuple are the same.
11.	Write a Python program to find the third largest number from a given list of numbers.

Predict out:
Q)
set1={2,5,3}

set2={3,1}

set3={}

set3=set1&set2

print(set3)


Q)
list1=[1,3,4,2]

x=list1.pop(2)

print(set([x]))


Q)
set1={"a",3,"b",3}

set1.remove(3)


Write a program to print an element, if the element is present in two lists(both lists are of same data type,
integers and ordered lists) without using nested for loops

"""

# #Write a python program to find the common numbers from two lists
#
# lst1=list(map(int,input("enter list 1 : ").split()))
# lst2=list(map(int,input("enter list 2 :").split()))
#
# n1=[x for x in lst1 if x in lst2]
# print(str(n1)[1:-1])



# Write a program to print an element, if the element is present in two lists(both lists are of same data type,
# integers and ordered lists) without using nested for loops

lst1=list(map(int,input("enter list 1 : ").split()))
lst2=list(map(int,input("enter list 2 :").split()))
n=int(input("enter the number"))

if n in lst1 and n in lst2:
    print(f'{n} is present in both lists')
else:
    print(f'{n} is not in both lists')






