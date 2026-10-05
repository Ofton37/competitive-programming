import sys
def generate_g(n):
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    
    G.reverse()
    return G

def insertionsort(A,n,g):
    cnt = 0
    for i in range(g,n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g]=A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt
        
def shellSort(A, n):
    G = generate_g(n)
    m = len(G)
    total=0
    for i in range(m):
        total+=insertionsort(A,n,G[i])
    print(m)
    print(*G)
    print(total)
    for x in A:
        print(x)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    A= [int(x) for x in input_data[1:n+1]]
    
    shellSort(A, n)
    
if __name__ == '__main__':
    solve()    
    