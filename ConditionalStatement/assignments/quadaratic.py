# Roots of Quadratic Equation
# root x = (-b +- sqrt(b^2 - 4ac))/(2a)
import math

print("Enter coefficients a, b and c: ");
a=int(input())
b=int(input())
c=int(input())
discriminant = b * b - 4 * a * c;
print("discriminant",discriminant)

if discriminant==0:
    # condition for real and equal roots
    root1 = root2 = -b/(2*a)
    print("root1 =  root2 = ", root2);

elif discriminant > 0:
    # condition for real and distinct root
    root1 = (-b + math.sqrt(discriminant)) / (2 * a);
    root2 = (-b - math.sqrt(discriminant)) / (2 * a);
    print("root1 = ", root1, " root2 = " ,root2);
else:
    #complex root
    realPart = -b / (2 * a);
    imaginaryPart= math.sqrt(-discriminant)/(2*a)
    print("root1 = ", realPart,"+i" ,imaginaryPart, "root2 = ",realPart,"-i", imaginaryPart);

