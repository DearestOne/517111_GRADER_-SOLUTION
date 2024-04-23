x = int(input())
y = int(input())
sumX = 0
sumY = 0
sumXY = 0
while True:
    num = int(input())
    if num <= 0:
        break
    if num % x == 0 and num % y != 0:
        sumX += num
    elif num % y == 0 and num % x != 0:
        sumY += num
    if num % y == 0 or num % x == 0:
        sumXY += num
print(sumX)
print(sumY)
print(sumXY)