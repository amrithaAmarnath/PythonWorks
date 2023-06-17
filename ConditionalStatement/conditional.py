#a = 48;b = 50;
"""
a=int(input("enter the first number"));
b=int(input("enter the second number"));
c=int(input("enter the third number"));


if a < b:
    print("a is not greater than b");

if a > b:
    print("a is grater than b");
else:
    print("a is not greater than b")

if a > b and a > c:
    print("a is greater than b and c");
elif a==b or b < c:
    print("a and b are same or b less than c");
else:
    print("a is not greater than b")
"""

c=input("Enter the choice + - * / ");

a = int(input("Enter a ="));
b = int(input("Enter b ="));



if c == '+':
    print("sum is",a+b);
elif c == '-':
    print("difference is",a-b);
elif c == '*':
    print("product is",a * b);
elif c == '/':
    print("Division is",a / b);
else:
    print("invalid input");