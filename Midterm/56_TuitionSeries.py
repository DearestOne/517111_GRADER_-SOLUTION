start, vat, year = input().split()
start, vat, year = float(start),int(vat),int(year)
total = 0
total_vat = start * (vat / 100)
for i in range(year):
    print("%.1f"%start)
    total += start
    start += total_vat
print("%.1f"%total)