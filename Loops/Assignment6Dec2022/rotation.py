#circular rotation of an array by k position
arr = [1,2,3,4,5]

k=3
i=0
while i < k:
    arr = [arr[-1]] + arr[0:-1]
    print(arr)
    i += 1
