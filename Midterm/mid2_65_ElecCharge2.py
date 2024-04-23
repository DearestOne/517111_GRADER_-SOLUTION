w, x, y, z = [ int(e) for e in input().split() ]
if y == 1:
    w += z
    if w > x:
        print(x,"over")
    else:
        print(w,"okay")
else:
    w -= z
    if w < 0:
        print("0 under")
    else:
        print(w,"okay")