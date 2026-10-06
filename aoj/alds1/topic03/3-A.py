def toRPN(A,n):
    Stack = []
    for token in A:
        if token == "+":
            b = Stack.pop()
            a = Stack.pop()
            Stack.append(a + b)
        elif token == "-":
            b = Stack.pop()
            a = Stack.pop()
            Stack.append(a - b)
        elif token == "*":
            b = Stack.pop()
            a = Stack.pop()
            Stack.append(a * b)
        else:
            Stack.append(int(token))
    return Stack.pop()

def solve():
    Data = input().split()
    n =  len(Data)
    result = toRPN(Data,n)
    print(result)


if __name__ == '__main__':
    solve()    