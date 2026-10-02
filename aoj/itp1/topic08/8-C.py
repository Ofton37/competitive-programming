c = [0] * 26
while True:
    try:
        s = input()
    except EOFError:
        break

    for ch in s:
        if ch.isupper():
            ch = ch.lower()
        if 'a' <= ch <= 'z':       
            num = ord(ch) - ord('a')
            c[num] += 1

for i in range(26):
    alpha = chr(ord('a') + i)
    print(f"{alpha} : {c[i]}")