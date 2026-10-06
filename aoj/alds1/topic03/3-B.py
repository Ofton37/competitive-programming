from collections import deque

def RRS(queue,q):
    total = 0
    while queue:
        p, time = queue.popleft()
        
        if time <= q:
            total += time
            print(f"{p} {total}")
        else:
            total += q
            queue.append([p,time-q])
    
def solve():
    n,q = map(int,input().split())
    queue = deque()
    for _ in range(n):
        p, time= input().split()
        queue.append([p,int(time)])
    RRS(queue,q)    

solve()