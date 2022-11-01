def find(l:list, x, y, n, m):
    global d
    if d[x][y]:
        return d[x][y]
    res = 1
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        if 0<=x+dx<=n-1 and 0<=y+dy<=m-1 and l[x][y]<l[x+dx][y+dy]:
            res =max (res,  find(l,x+dx,y+dy,n,m) + 1)
    d[x][y] = res
    return res
if __name__ == '__main__':
        
    #[[1,2,3],
    # [4,5,6],
    # [7,8,9]]
    # matrix = [[1,2],[4,3]]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[4,3,3,6,6,3,2,1,0,7],[1,8,2,8,5,9,2,8,3,1],[8,0,9,2,4,3,2,4,3,7],[1,2,2,6,3,0,3,9,7,0],[7,4,3,8,8,3,2,4,6,8],[2,8,9,2,9,3,0,8,7,8],[8,9,9,4,6,3,3,4,9,6],[2,8,3,8,1,3,7,3,0,7],[2,1,1,6,4,1,0,8,1,6],[4,1,3,6,3,4,4,4,0,3]]
    n = len(matrix)
    m = len(matrix[0])
    b = 0
    d = []
    for _ in range(n):
        d.append([0]*m)

    for x in range(n):
        for y in range(m):
            if d[x][y]:
                continue
            b = max(find(matrix, x, y, n, m), b)
    print(b)
    print(d)