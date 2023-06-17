m1=int(input("enter marks for Physics out of 100"))
m2=int(input("enter marks for Chemistry out of 100"))
m3=int(input("enter marks for Biology out of 100"))
m4=int(input("enter marks for Maths out of 100"))
m5=int(input("enter marks for Computer out of 100"))
s=m1+m2+m3+m4+m5
p= (s/500 *100)
print("percentage = ",p,"%")
if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")