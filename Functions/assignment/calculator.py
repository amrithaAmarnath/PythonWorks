def sum(a, b):
    return a+b

def diff(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def exp(a,b):
    return a**b

ch = 'y'

while ch == 'Y' or ch == 'y':
    a = int(input('enter first number'))
    b = int(input('enter second number'))
    op = input('enter operator +, -, *, /, **')

    if op == '+':
        c = sum(a, b)
    elif op == '-':
        c = diff(a, b)
    elif op == '*':
        c = multiply(a, b)
    elif op == '/':
        c = division(a, b)
    elif op == '**':
        c = exp(a, b)
    else:
        print('invalid operator')

    print(f'{a} {op} {b} = {c}')
    ch = input("enter Y or y to continue")

