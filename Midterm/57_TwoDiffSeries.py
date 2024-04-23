x,y = input().split()
x,y = int(x),int(y)
is_plus = False
total = 0
for i in range(y):
    total += x
    if is_plus == False:
        x *= 4
        is_plus = True
    else:
        x += 10
        is_plus = False
print(total)