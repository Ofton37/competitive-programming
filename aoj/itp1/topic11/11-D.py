def roll_N(d): return [d[1], d[5], d[2], d[3], d[0], d[4]]
def roll_E(d): return [d[3], d[1], d[0], d[5], d[4], d[2]]
def roll_R(d): return [d[0], d[2], d[4], d[1], d[3], d[5]]

def is_same_dice(dice1,dice2):
    cur = dice1[:]
    moves = ['', 'N', 'N', 'N', 'E', 'EE']
    for move in moves:
        for m in move:
            if m == 'N':
                cur = roll_N(cur)
            elif m == 'E':
                cur = roll_E(cur)

        for _ in range(4):
            if cur == dice2:
                return True
            cur = roll_R(cur)
        
    return False
def solve():
    n = input()
    dice = [list(map(int, input().split())) for _ in range(int(n))]
    for i in range(int(n)):
        for j in range(i+1,int(n)):
            if is_same_dice(dice[i],dice[j]):
                print("No")
                return
    
    print("Yes")

solve()
