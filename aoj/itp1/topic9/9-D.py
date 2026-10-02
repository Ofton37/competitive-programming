s = list(input())
x = int(input())
for i in range(x):
    q = input().split()
    cmd = q[0]
    a = int(q[1])
    b = int(q[2])+1
    if cmd == 'print':
        print("".join(s[a:b]))
    if cmd == 'reverse':
        s[a:b] = s[a:b][::-1]
    if cmd == 'replace':
        p = q[3]
        s[a:b] = p