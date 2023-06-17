"""
1.write a pyhton function to find the max of three no:s
2. write a pyhton function to sum all the numbers in a list
3. write a pyhton function to multiply all the numbers in a list


"""
#Q1
def maximum(a,b,c):
    return max(a,b,c)


a=100
b=25
c=5
print(maximum(a,b,c))

#Q2
def sumlist(lst):
    s=0
    for i in lst:
        s += i
    return s


lst=[1,2,3,4,5,6]
print(f'sum of list items is {sumlist(lst)}')

#Q3
def productlist(lst):
    p=1
    for i in lst:
        p *= i
    return p


lst=[1,2,3,4,5,6]
print(f'product of list items is {productlist(lst)}')

#Square of a number

def square(a):
    return a**2


n = int(input("Enter a number"))
print(f'Square of {n} = ', square(n))

#Square of a number in a list

def squarelist(a):
    sq = []
    for i in a:
        sq.append(i ** 2)
    #return sq
    sqsum = sumlist(sq)
    return sq,sqsum


lst1 = [1,2,3,4,5,6]
sqlist,sqsum = squarelist(lst1)
#print(f'Square of {lst1} = ', squarelist(lst1))
print(f'Square of {lst1} = ', sqlist)
print(f'Sum of Square of list {lst1} = ', sqsum)






