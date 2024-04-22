n = int(input())
i = 0
while i < n:
    height = int(input())
    if height < 101:
        print(0)
    elif 101 <= height <= 130:
        print(120)
    elif height >= 131:
        print(450)
    i += 1