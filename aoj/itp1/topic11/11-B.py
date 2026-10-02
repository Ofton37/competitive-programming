dice = list(map(int,input().split()))
right_face_map = {
    (dice[0], dice[1]): dice[2], (dice[0], dice[2]): dice[4], (dice[0], dice[4]): dice[3], (dice[0], dice[3]): dice[1],
    (dice[1], dice[0]): dice[3], (dice[1], dice[3]): dice[5], (dice[1], dice[5]): dice[2], (dice[1], dice[2]): dice[0],
    (dice[2], dice[0]): dice[1], (dice[2], dice[1]): dice[5], (dice[2], dice[5]): dice[4], (dice[2], dice[4]): dice[0],
    (dice[3], dice[0]): dice[4], (dice[3], dice[4]): dice[5], (dice[3], dice[5]): dice[1], (dice[3], dice[1]): dice[0],
    (dice[4], dice[0]): dice[2], (dice[4], dice[2]): dice[5], (dice[4], dice[5]): dice[3], (dice[4], dice[3]): dice[0],
    (dice[5], dice[1]): dice[3], (dice[5], dice[3]): dice[4], (dice[5], dice[4]): dice[2], (dice[5], dice[2]): dice[1],
}
n = input()
for i in range(int(n)):
    t,f= map(int,input().split())
    right = right_face_map[(t,f)]
    print(right)
