def bubblesort(x, n):
    cnt = 0
    flag = True
    
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
                cnt += 1
                flag = True  # 交換があったことを記録
                
    # ソートが完了してから最後に出力
    print(*x)
    print(cnt)

def solve():
    n = int(input())
    datas = list(map(int, input().split()))
    bubblesort(datas, n)

if __name__ == "__main__":
    solve()