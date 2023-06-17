"""MATRIX TRANSPOSE """

#Normal method

# matrix = [[1,2,3],
#           [4,5,6]]
matrix = [[1,2],
          [3,4],
          [5,6],
          [7,8]]

MT=[[0,0,0,0],[0,0,0,0]]
for i in range(len(matrix)): #range(4)
    for j in range(len(matrix[0])): #range(2)
        MT[j][i]=matrix[i][j]
        #print(matrix[i][j])

for r in MT:
   print(r)


#using List Comprehension
matrix = [[1,2],
          [3,4],
          [5,6],
          [7,8]]
MT=[]

MT=[[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
for r in MT:
   print(r)