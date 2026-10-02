def max_check(x,n):
    minv=x[0]
    maxv = -1000000000
    for i in range(1,n):
        if  x[i] - minv > maxv:
            maxv = x [i] - minv
        if x[i] < minv:
            minv = x[i]
    return maxv

def solve():
    n = int(input())
    datas = [0]*n
    for i in range(n):
        datas[i]=int(input())   
    MAX = max_check(datas,n)
    print(MAX)
solve()
