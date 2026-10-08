import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    dictionary = set()
    
    output = []
    idx = 1
    for _ in range(n):
        o = input_data[idx]
        c = input_data[idx + 1]
        idx += 2
        if o == "insert":
            dictionary.add(c)
        else:
            if c in dictionary:
                output.append("yes")
            else:
                output.append("no")
    print("\n".join(output)) 
solve()