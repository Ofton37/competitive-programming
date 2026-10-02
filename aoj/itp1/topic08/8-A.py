s = input()

for ch in s:
    if ch.islower():
        print(ch.upper(),end="")
    elif ch.isupper():
        print(ch.lower(),end="")
    else:
        print(ch,end="")
print()
