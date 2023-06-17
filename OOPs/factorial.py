#fact using class with function and return value

class Factorial:
    def fact(self,n):
        if n == 1:
            return 1
        else: #both return statement mention below are correct
           # return n*self.fact(n-1)
            return n * Factorial.fact(self, n -1)

# f = 1
        # while n > 0:
        #     f= f*n
        #     n=n-1
        # return f


n=int(input("enter number"))
obj=Factorial()
print(f"factorial of {n} is {obj.fact(n)}")