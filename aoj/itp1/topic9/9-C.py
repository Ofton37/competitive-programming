cnt = int(input())
point = [0]*2
for i in range(cnt):
    str1,str2 = input().split()
    if str1 == str2:
        point[0] += 1
        point[1] += 1
    elif str1 > str2:
        point[0] += 3
    elif str1 < str2:
        point[1] += 3
print(*point)
