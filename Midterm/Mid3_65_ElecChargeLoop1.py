n = int(input())
rcount = 0
for i in range(n):
    x,y,z = input().split()
    x,y,z = int(x),int(y),int(z)
    if y == 1:
        print(x + z)
    elif x > z:
        print(x - z)
    else:
        print("reset 0")
        rcount += 1
print(rcount)
