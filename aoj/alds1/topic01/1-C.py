import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solve():
    n = int(input())
    datas = [0]*n
    for i in range(n):
        datas[i]=int(input())   
    cnt = sum(1 for x in datas if is_prime(x))
    print(cnt)
solve()