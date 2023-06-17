#6.	 Write a python program to create a list of even numbers and another list of odd numbers from a given list
lst=[ 1, 20 , 15, 4, 80, 11, 25, 100]
print(f'original list = {lst}')
ev=[x for x in lst if x % 2 == 0]
od=[x for x in lst if x % 2 != 0]
print(f'even: {ev} \n odd: {od}')
