# 给个矩阵，0代表海，1代表陆地，把所有岛替换成海（能连到边上的不算岛）


def replace_sea(matrix):
    if matrix == None or len(matrix) == 0:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    visited = [[0 for _  in range(m)] for _ in range(n)]

    # step 1 :replace the all 1 with '-'

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 :
                matrix[i][j] = '-'


    # call for flood fill for all "-" on the edges
    for i in range(n):
        if matrix[i][0] == "-":
            flood(matrix,i ,0 )


    for i in range(n):
        if matrix[i][m-1] == "-":
            flood(matrix, i, m-1)

    for j in range(m):
        if matrix[0][j] == "-":
            flood(matrix, 0, j)

    for j in range(n):
        if matrix[n-1][j] == "-":
            flood(matrix,n-1,j )


    # step3 replace all '-' with 'x'

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '-':
                matrix[i][j] = 1



def flood(mat,x,y):
    m = len(mat)
    n = len(mat[0])
    if x < 0 or x > m-1 or y < 0 or y > n-1:
        return

    if mat[x][y] != '-':
        return
    mat[x][y] = 1

    flood (mat, x + 1, y)
    flood(mat, x-1, y)
    flood(mat, x, y+1)
    flood(mat, x,  y-1)