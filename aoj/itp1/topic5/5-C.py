while True:
    h,w = map(int,input().split())
    if h == 0 and w ==0:
        break
    for i in range(h):
        if i % 2 == 0:
            print("#."*(w//2),end="")
            if w % 2 != 0:
                print("#",end="")
            print()
        else:
            print(".#"*(w//2),end="")
            if w % 2 != 0:
                print(".",end="")
            print()
    print()