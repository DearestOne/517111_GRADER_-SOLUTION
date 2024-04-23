Max = 0
Min = 50000
while True:
    num = int(input())
    if num <= 0:
        break
    elif num % 2 == 1:
        if num > Max:
            Max = num
        if num < Min:
            Min = num
print(Max)
print(Min)
print(Max - Min)
