# 1.Write a python program to convert  a   string to tuple
# st1 = "Luminar"
# tpl = tuple(st1)
# print(tpl)

# 2.Write a python program to convert a list to a tuple
# lst = [1, 2, 3, ["hai","hello"]]
# tp = tuple(lst)
# print(tp)

#tp = [25,12,50,10,50,25,5]
#tp = tuple(input("enter a tuple").split())

# user input as tuple as given below
#user_input = input("enter space separated integers") # enter input as string
#tp = tuple(int(i) for i in user_input.split())


# 3.Write a python program to find repeated items from a tuple
tp = (25,12,50,10,50,25,5)
print("tuple = ",tp)
c = set()
for i in tp:
    if tp.count(i) > 1:
        c.add(i)
print(f' Repeated elements in tuple {tuple(c)}')

#tp=[]
# for i in user_input.split():
#     tp.append(int(i))
# tp = tuple(tp)
#print("tuple tp=",tuple(tp))


