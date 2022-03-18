A = [[6,8,3],
    [2,5,3],
    [0,4,8]]
B = [[7,0],
    [8,3],
    [2,8]]
C=  [[0,0],
    [0,0],
    [0,0]]
for i in range(0,len(C)):
    for j in range(0,len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(row)
