my_list = [int(e) for e in input().split()]
num = 10
total = 0
for i in my_list:
    total += i * num
    num -= 1
need = 11 - (total % 11)
if need != 11:
    print(need)
else:
    print(0)