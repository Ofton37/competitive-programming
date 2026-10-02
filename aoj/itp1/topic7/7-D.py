n,m,l = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grid2 = [list(map(int, input().split())) for _ in range(m)]
c = [[0] * l for _ in range(n)]
for i in range(n):
    for k in range(l):
        for j in range(m):
            c[i][k] += grid[i][j]*grid2[j][k]
        
for i in range(n):
    print(*c[i])

