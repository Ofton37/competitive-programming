import math

def solve():
    n,k = map(int,input().split())
    W = []
    total = 0
    cnt = 0
    for i in range(n):
        num = int(input())
        total += num
        cnt += 1
        W[i] = num
        
    upp = math.ceil(total/k)
    if upp > max(W):
        print(upp)
    else:
        print(max(W))

solve()
    