r,c = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
grid2 = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(r):
    for j in range(c):
        grid2[i][j] = grid[i][j]
        grid2[i][c] += grid[i][j]
        grid2[r][j] += grid[i][j]
        grid2[r][c] += grid[i][j]
for i in range(r + 1):
    print(*grid2[i])
