my_list = [int(e) for e in input().split()]
num = 10
total = 0
for i in my_list:
    total += i * num
    num -= 1
print(total)