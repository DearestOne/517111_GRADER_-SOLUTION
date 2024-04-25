# input
n = int(input())
my_list = []
for i in range(n-1):
    inner_list = [int(e) for e in input().split()]
    my_list.append(inner_list)

# output
for i in range(n):
    for j in range(n):
        if j == i:
            print("0", end = " ")
        elif i > j:
            print(my_list[i-1][j],end = " ")
            #print("I",end = " ")
        elif j > i:
            print(my_list[j-1][i],end = " ")
            #print("J",end = " ")
    print()
    
# ยากสุด
