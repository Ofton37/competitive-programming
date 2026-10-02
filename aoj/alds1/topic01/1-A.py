def sort(A,n):
    for i in range(n):
        v = A[i]
        j = i-1
        while j >= 0 and A[j] > v:
            A[j+1]=A[j]
            j -= 1
        A[j+1] = v
        print(*A)

def solve():
    n = int(input())
    datas = list(map(int,input().split()))
    sort(datas,n)
    
solve()
