while True:
    data = list(map(int,input().split()))
    if data[0] == 0 and data[1] == 0:
        break
    else:
        data.sort()
        print(data[0], data[1])
