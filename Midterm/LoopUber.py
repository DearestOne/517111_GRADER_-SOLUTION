while True:
    x,y = input().split()
    x,y = int(x),int(y)
    if x <= 0 or y <= 0:
        break
    else:
        print("%.2f"%(25 + (4.50*x) + y))