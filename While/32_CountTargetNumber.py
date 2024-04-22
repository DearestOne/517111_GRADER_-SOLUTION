target = int(input())
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    elif x == target:
        count += 1
if count == 0:
    print("None")
else:
    print(count)