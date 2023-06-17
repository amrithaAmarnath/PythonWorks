
c=input("select the operations to perform \n 1 for '+' \n 2 for '-' \n 3 for '*' \n 4 for '/' \n 5 for '%' "
        " \n 6 for '//' \n 7 for '**' \n 8 for '==' \n 9 for '!=' \n 10 for '>' \n 11 for '<' "
        "\n 12 for '<=' \n 13 for '>=' \n 14 for AND' \n 15 for OR' \n 16 for NOT'");

d={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'};
if c in (d):
    a = int(input("Enter a ="));
    b = int(input("Enter b ="));
else:
    print("invalid input");

if c == '1':
    print(a+b);
if c == '2':
    print(a-b);
if c == '3':
    print(a * b);
if c == '4':
    print(a / b);
if c == '5':
    print(a % b);
if c == '6':
    print(a // b);
if c == '7':
    print(a ** b);

if c== '8':
    print(a==b);
if c == '9':
    print(a != b);
if c == '10':
    print(a > b);

if c == '11':
    print(a < b);

if c == '12':
    print(a <= b);

if c == '13':
    print(a >= b);
if c == '14':
    print(a>5 and b <3);

if c == '15':
    print(a > 5 or a < 2);

if c == '16':
    print(not(a > 3 and a < 10));




"""
a=10;b=5;


print("sum = ");print(a+b);
print("subtraction = ");print(a-b);
print("Multiplication");print(a*b);
print("division");print(a/b);
print("modulus");print(a%b);
print("integerDivision");print(a // b);
print("Exponential");print(a ** b);
print("equality checking");print(a==b);

print("not equality checking");print(a!=b);
print("greater than checking");print(a>b);
print("less than checking");print(a<b);
print("less than or equal"); print(a<=b);
print("greater than or equal"); print(a>=b)
print("AND operation :"); print(a>5 and b <3);
print("OR operation :");print(a > 5 or a < 2);
print("NOT operation :");print(not(a > 3 and a < 10));

"""









