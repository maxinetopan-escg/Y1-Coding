# 1 +
# for each off number from 3 - 1001 (inc.)
    # n = length of side
    # tr = n**2 (top right)
    # tl = tr - (n - 1) (top left)
    # bl = tl - (n - 1)
    # br = bl - (n - 1)

diagSum = 1

for i in range(3, 1002, 2):
    l = i - 1
    tr = i**2
    tl = tr - l
    bl = tl - l
    br = bl - l
    diagSum += tr + tl + bl + br

print(diagSum)