x,y = input().split()
x,y = int(x),int(y)
total = 0
while True:
    num = int(input())
    if num <= 0:
        break
    elif x <= num <= y or y <= num <= x:
        total += num
print(total)
