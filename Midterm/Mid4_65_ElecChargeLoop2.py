n = int(input())
current = int(input())
for i in range(n):
    x,y = input().split()
    x,y = int(x),int(y)
    if x == 1:
        current += y
    else:
        if current < y:
            current = 0
        else:
            current -= y
    print(current)