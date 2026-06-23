#d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
c = ""
i = 0
while len(c) <= 10 ** 6:
    c += str(i)
    i += 1

calc = int(c[1]) * int(c[10]) * int(c[100]) * int(c[1000]) * int(c[10000]) * int(c[100000]) * int(c[1000000])
print(calc)