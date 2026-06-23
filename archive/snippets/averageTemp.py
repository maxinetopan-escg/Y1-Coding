maxTemps = []
totalAverage = 0
negativesCount = 0
maxTemp = 0

# get min and max temps
minTemp = float(input("please enter min temp: "))
maxTemp = float(input("please enter max temp: "))

while maxTemp != 999:
    # calc avg temp
    avgTemp = (minTemp + maxTemp) / 2
    totalAverage = totalAverage + avgTemp

    # add maxTemp to a list
    maxTemps.append(maxTemp)

    if minTemp < 0:
        negativesCount = negativesCount + 1
    
    # get min and max temps
    minTemp = float(input("please enter min temp: "))
    maxTemp = float(input("please enter max temp: "))

overallAverage = totalAverage / len(maxTemps)

daysOverAvg = 0
for temp in maxTemps:
    if temp > daysOverAvg:
        daysOverAvg = daysOverAvg + 1

print(f"negatives: {negativesCount}, Days above avg: {daysOverAvg}")