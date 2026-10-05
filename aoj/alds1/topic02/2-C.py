def isStable(In ,Out, n):
    for i in range(n):
        if In[i][0] != Out[i][0]:
            return False
    return True
    
def bubblesort(A, n):
    Cards = A.copy()
    
    for i in range(n):
        for j in range(n - 1, i, -1):
            if int(Cards[j][1]) < int(Cards[j - 1][1]):
                Cards[j], Cards[j - 1] = Cards[j - 1], Cards[j]
    
    return Cards 
                
def selectionsort(A, n):
    Cards = A.copy()
    for i in range(n):
        minj = i
        # i から n-1 までの範囲で最小値のインデックスを探す
        for j in range(i, n):
            if int(Cards[j][1]) < int(Cards[minj][1]):
                minj = j
        
        if i != minj:  # 自分自身と入れ替える場合はカウントしない
            Cards[i], Cards[minj] = Cards[minj], Cards[i]

    return Cards
            
def solve():
    n = int(input())
    Datas = input().split()
    Bubble = bubblesort(Datas, n)
    Select = selectionsort(Datas, n)
    print(*Bubble)
    print("Stable")
    print(*Select)
    if isStable(Bubble, Select, n):
        print("Stable")
    else:
        print("Not stable")
        
solve()