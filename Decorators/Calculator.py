def calculator(func):
    def inner(a,b):
        print(f'{a}{op}{b} is ')
        return func(a,b)
    return inner

@calculator
def divide(a,b):
    print(a/b)
@calculator
def sum(a,b):
    print(a+b)
@calculator
def multiply(a,b):
    print(a*b)
@calculator
def diff(a, b):
    print(a - b)

@calculator
def exp(a, b):
    print(a, "**",b,"=",a ** b)

ch='y'
while ch == 'Y' or ch == 'y':
    a = int(input('enter first number'))
    b = int(input('enter second number'))
    op = input('enter operator +, -, *, /, **')

    if op == '+':
        sum(a, b)
    elif op == '-':
        diff(a, b)
    elif op == '*':
        multiply(a, b)
    elif op == '/':
        divide(a, b)
    elif op == '**':
        exp(a, b)
    else:
        print('invalid operator')

    ch = input("enter Y or y to continue")


# Another method


# def calculator(func):
#     def addition():
#
#     return addition






