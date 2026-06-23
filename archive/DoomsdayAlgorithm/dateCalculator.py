import constants as c

def GetCenturyAnchor(year):
    century = year//100
    cIndex = century % 4
    return c.C_ANCHORS[cIndex]

def GetDoomsdayForYear(year):
    cAnchor = GetCenturyAnchor(year)
    lastTwoYear = year % 100
    if lastTwoYear % 2 == 1:
        lastTwoYear += 11
    lastTwoYear /= 2
    if lastTwoYear % 2 == 1:
        lastTwoYear += 11
    lastTwoYear %= 7
    return ((7 - lastTwoYear) + cAnchor) % 7

print(GetDoomsdayForYear(1998))