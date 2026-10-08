def solve():
    n = int(input())
    S = set(map(int, input().split()))  # set に変更
    q = int(input())
    T = list(map(int, input().split()))
    
    # T の要素のうち S に含まれるものの個数をカウント
    cnt = sum(1 for num in T if num in S)
    print(cnt)

solve()