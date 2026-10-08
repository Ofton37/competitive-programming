import sys

def execute(A):
    Stack1 = []
    Stack2 = []
    for i,char in enumerate(A):
        if char == "\\":
            Stack1.append(i)
        elif A[i] == "/":
            if Stack1:
                j = Stack1.pop()
                a = i - j 
                while Stack2 and Stack2[-1][0] > j:
                    a += Stack2.pop()[1]
                    
                Stack2.append([j, a])
                
    # 総面積
    total_area = sum(area for _, area in Stack2)
    # 各水たまりの面積のリスト
    k_areas = [area for _, area in Stack2]
    
    # 1行目: 総面積
    print(total_area)
    # 2行目: 水たまりの数 と 各面積（スペース区切り）
    print(len(k_areas), *k_areas)  
                        
    
def solve():
    input_data = sys.stdin.read().split()
    execute(input_data[0])

solve()