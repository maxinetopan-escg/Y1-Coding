# set the variable to a placeholder value
userNum = -1

while userNum < 0:
    try: # if there is an error from trying to cast an invalid value to an int
        userNum = int(input("please enter a positive integer: "))
    except: # go here to handle the error
        pass # loop around with the while loop again

incCount = 0
decCount = 0

# convert user num to a string for easier parsing through the digits (treated as a list of characters)
userNumStr = str(userNum)

for i in range(1, len(userNumStr)):
    # get the current and previous characters and convert them to ints
    prevNum = int(userNumStr[i - 1])
    currNum = int(userNumStr[i])

    if prevNum > currNum:
        decCount += 1
    elif currNum > prevNum:
        incCount += 1

if (incCount == decCount and incCount > 0):
    print("perfectly bouncy number")
elif (incCount == 0 or decCount == 0): # if either are 0, the number is increasing/decreasing/both so it is not bouncy
    print("not bouncy")
else:
    print("bouncy number")
