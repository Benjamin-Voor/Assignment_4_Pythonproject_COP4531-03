# F[M, N]
# row, column
# i, j

M = 4+1 # rows
N = 5+1 # columns
C = [ [0]*N for i in range(M)]
C[1][2] = 5 # at row 0, column 1, lies 5
C[1][4] = 2
C[2][1] = 3
C[2][3] = 1
C[3][2] = 7
C[3][5] = 4
C[4][1] = 4
C[4][4] = 8

F = [ [0]*N for i in range(M)]
F[1][1] = C[1][1]
    # F[1,1] = C[1,1];

for column in range(N):
    if column == 0 or column == 1:
        continue
    # for(j=2; j<=m; j++)
    F[1][column] = F[1][column - 1] + C[1][column] # previous column plus current cell
    # F[1, j] = F[1, j-1] + C[1, j];

for row in range(M):
    if row == 0 or row == 1:
        continue
    # for(i=2; i<=n; i++)
    F[row][1] = F[row - 1][1] + C[row][1] # previous row plus current cell
        # F[i, 1] = F[i-1, 1] + C[i, 1];
    for column in range(N):
        if column == 0 or column == 1:
            continue
        # for(j= 2; j<= m; j++)
        F[row][column] = max(F[row - 1][column], (F[row][column - 1] + C[row][column]))
        # F[i, j] = max(F[i-1, j], F[i, j-1]) + C[i, j]
print('C', C)
print('F', F)
    # return F[n,m]
# Time complexity: O(nm)