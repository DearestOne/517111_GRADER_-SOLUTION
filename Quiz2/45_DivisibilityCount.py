x = int(input())
y = int(input())
countX = 0
countY = 0
countXY = 0
while True:
    num = int(input())
    if num <= 0:
        break
    if num % x == 0 and num % y != 0:
        countX += 1
    elif num % y == 0 and num % x != 0:
        countY += 1
    if num % y == 0 or num % x == 0:
        countXY += 1
print(countX)
print(countY)
print(countXY)