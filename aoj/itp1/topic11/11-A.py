dice = list(map(int,input().split()))
cmd = input()
for c in cmd:
    if c == 'S':
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif c == 'W':
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif c == 'E':
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif c == 'N':
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
print(dice[0])
