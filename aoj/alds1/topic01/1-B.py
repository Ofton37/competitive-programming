import math

def solve():
    x,y = map(int,input().split())
    ans = math.gcd(x,y)
    print(ans)
solve()
