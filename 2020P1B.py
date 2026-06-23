numOfDigs = int(input('how many digits to enter: '))

freq = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0
    }

for i in range(numOfDigs):
    num = int(input("please enter digit: "))
    freq[num] += 1

maxFreqVal = 0
maxFreqKey = None

for i in range(10):
    if freq[i] > maxFreqVal:
        maxFreqVal = freq[i]
        maxFreqKey = i
    elif freq[i] == maxFreqVal:
        maxFreqKey = "data was multimodal"

print(maxFreqKey)