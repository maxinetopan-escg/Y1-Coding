# adding a comment to show what Git does
while True:
    try:
        userstr = input("please enter an integer greater than 0: ")
        userint = int(userstr)
        if userint > 0:
            break
    except:
        pass

incCount = 0
decCount = 0
increasing = True
decreasing = True

for i in range(1, len(userstr)):
    prev = int(userstr[i-1])
    curr = int(userstr[i])

    if prev >= curr:
        decCount += 1
    if prev <= curr:
        incCount += 1

if incCount > 0 and decCount == 0:
    print