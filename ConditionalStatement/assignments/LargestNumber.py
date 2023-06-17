x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=int(input("enter 3rd number"))

if x > y:
    if x > z:
       print("Largest no: is ", x)
    else:
        print("Largest no: is ", z)
elif y > z:
    print("Largest no: is" , y)
else:
    print("Largest no: is ", z)
