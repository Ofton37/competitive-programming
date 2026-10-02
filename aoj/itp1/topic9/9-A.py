cnt = 0
search = input().lower()
while True:
    words = input().split()
    if words[0] == "END_OF_TEXT":
        break
    for ch in words:
        if ch.lower() == search:
            cnt += 1        
print(cnt)