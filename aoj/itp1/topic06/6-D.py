n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
vec = [int(input()) for _ in range(m)]

for i in range(n):
    c = 0
    for j in range(m):
        c += mat[i][j]*vec[j] 
    print(c)
