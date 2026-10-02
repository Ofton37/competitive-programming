import math
while True:
    n = input()
    if int(n) == 0:
        break
    datas = list(map(int,input().split()))
    total = sum(datas)
    size = len(datas)
    avg = total/size
    al = 0
    for i in datas:
        al += (i - avg)**2
    a = abs(math.sqrt(al/size))
    print(a)
