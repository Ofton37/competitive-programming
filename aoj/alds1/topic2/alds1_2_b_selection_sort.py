def selectionsort(x, n):
    cnt = 0
    for i in range(n):
        minj = i
        # i から n-1 までの範囲で最小値のインデックスを探す
        for j in range(i, n):
            if x[j] < x[minj]:
                minj = j
        
        # 最小値が見つかったら、ループを出てから 1 回だけ交換する
        if i != minj:  # 自分自身と入れ替える場合はカウントしない
            x[i], x[minj] = x[minj], x[i]
            cnt += 1

    print(*x)
    print(cnt)

def solve():
    n = int(input())
    datas = list(map(int, input().split()))
    selectionsort(datas, n)


solve()