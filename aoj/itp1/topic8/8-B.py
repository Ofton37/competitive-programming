while True:
    x = input()
    if int(x) == 0:
        break
    sum = 0
    for d in x:
        sum += int(d)
    print(sum)
