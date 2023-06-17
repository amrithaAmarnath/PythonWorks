#GCD of numbers

n = map(int, input().split())
list1 = list(n)
length = len(list1)
factors = []

for k in list1:
    for i in range(1,k+1):
        if k % i == 0:
            factors.append(i)
cf = []
for i in factors:
   # print(factors.count(i))
    if (factors.count(i) == length) and (i not in cf):
        cf.append(i)

#print(f'factors {factors}')
print(f'common factors {cf}')
print(f' gcd is {cf[len(cf)-1]}')

