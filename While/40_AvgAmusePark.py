n = int(input())
i = 0
total = 0
while i < n:
    height = int(input())
    if height < 101:
        pass
    elif 101 <= height <= 130:
        total += 120
    elif height >= 131:
        total += 450
    i += 1
print(total)
print("%.2f"%(total/n))