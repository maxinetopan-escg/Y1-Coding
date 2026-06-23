import dateCalculator as dc

def getDayOfWeekForDate(date):
    day, month, year = formatDate(date)

def formatDate(originalDate):
    splitDate = originalDate.split("/") # input: "dd/mm/yyy" output: [dd, mm, yyyy]
    day = int(splitDate[0])
    month = int(splitDate[1])
    year = int(splitDate[2])
    return day, month, year

# Main program starts here
testVar = dc.testFunction()
print(dc.MY_TEST_CONSTANT)

userDate = input("please enter a date in format dd/mm/yyyy: ") # ask user for date (dd/mm/yyyy)
getDayOfWeekForDate(userDate)