highestPrimeFactor = -1
origNum = 600851475143

for i in range(origNum, 1, -1):
    # if it's not divisible, just skip
    if origNum % i != 0:
        continue

    # if we get here the number's divisible
    # now we need to check if it's prime
    if i % 2 == 0:
        continue

    factorCount = 0
    for j in range(1, (i) + 1):
        factorCount += 1
    
    # if this number is prime
    if factorCount == 2:
        highestPrimeFactor = i
        break

print(highestPrimeFactor)