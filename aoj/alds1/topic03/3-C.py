from collections import deque

def execute(A):
    Tlink = deque()
    while A:
        command = A.popleft()
        o = command[0]
        if o == "insert":
            c = command[1]
            Tlink.appendleft(c)
        elif o == "deleteFirst":
            Tlink.popleft()
        elif o == "deleteLast":
            Tlink.pop()    
        elif o == "delete":
            c = command[1]
            try:
                Tlink.remove(c)
            except ValueError:
                pass
    print(*Tlink)
            
    

def solve():
    n = int(input())
    Dlink = deque()
    for _ in range(n):
        line = input().split()
        order = line[0]
        if len(line) > 1:
            cnt = int(line[1])
            Dlink.append([order,cnt])
        else:
            Dlink.append([order,None])
            
    execute(Dlink)


solve()