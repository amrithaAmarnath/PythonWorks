#5.	 Write a python program to print all even numbers from a given list
lst=[ 1, 20 , 15, 4, 80, 11, 25, 100]
even=list(filter(lambda x:x%2 ==0,lst))
print(even)