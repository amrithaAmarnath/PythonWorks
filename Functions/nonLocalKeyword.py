"""
Python nonlocal Keyword:

- Make a function inside a function, which uses the variable x as a non local
 variable
- The nonlocal keyword is used to work with variables inside nested functions,
 where the variable should not belong to the inner function.

-Use the keyword nonlocal to declare that the variable is not local.
- nonlocal means "Neither local nor global"

"""
# Eg 1
def outerFn():
    x = 200
    def innerFn():
        nonlocal x
        x=100

    innerFn()
    return x
print(outerFn())

# Eg 2
name = "Arya"
def programming():
    def python():
        nonlocal name
        name = "Amritha"

    def mean_stack():
        global name
        name = "Lakshmi"

    def flutter():
        name = "Deepthi"
    name = "Sujith"
    python()
    mean_stack()
    print("Inside Fn >> coder is "+ name)

programming()
print("Ouside Fn >> coder is "+ name)