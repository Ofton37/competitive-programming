cnt = 0
a,b,c = map(int,input().split())
for x in range(a,b+1):
    if c % x == 0:
        cnt += 1
print(cnt)
