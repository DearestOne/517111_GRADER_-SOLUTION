Min = int(input())
Max = int(input())
count = 0
while True:
    x = int(input())
    if x <= 0:
        break
    elif x > Max or x < Min:
        count +=1
print(count)