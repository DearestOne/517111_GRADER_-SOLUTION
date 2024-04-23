x,y = input().split()
x,y = int(x),int(y)
total = 0
for i in range(x,y+1):
    pw = i + 1
    total += ((-1)**pw) * (2*i)
print(total)