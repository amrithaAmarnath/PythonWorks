n=5
k=1
for i in range(1,2*n):
    for j in range(1,2*n):
        if (i==j or i+j==2*n)and i <= n:
            print(i, end=' ')
        else:
            print('', end=' ')
        if (i == j or i+j == 2*n) and i > n:
            print((2*n)-i, end='')
        else:
            print(' ', end=' ')

    print()