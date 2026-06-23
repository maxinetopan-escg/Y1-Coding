def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
sum(10000)

# n = 10000
# total = 0
# for i in range(n, 0, -1):
#     total = total + i

# print(total)