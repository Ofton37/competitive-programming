def linesearch(S,T):
    cnt = 0
    for num1 in T:
        for num2 in S:
            if num1 == num2:
                cnt += 1
                break
    return cnt
                

def solve():
    n = int(input())
    S = list(map(int,input().split()))
    q = int(input())
    T = list(map(int,input().split()))
    total = linesearch(S,T)
    print(total)
solve()