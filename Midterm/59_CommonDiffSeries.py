a,d,n = [int(e) for e in input().split()]
total = 0
for i in range(n):
    total += a + (i * d)
print(total)