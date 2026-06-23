#     slow = 0
#     medium = 0
#     fast = 0
# INPUTDATA
#     timeTaken = USERINPUT
#     IF timeTaken = 0 GOTO PRINT
#     IF timeTaken < 30 GOTO UNDER30
#     IF timeTaken < 60 GOTO UNDER60
#     slow = slow + 1
#     GOTO INPUTDATA
# UNDER30
#     fast = fast + 1
#     GOTO INPUTDATA
# UNDER60
#     medium = medium + 1
#     GOTO INPUTDATA
# PRINT
#     OUTPUT fast, medium, slow

slow = 0
medium = 0
fast = 0

timetaken = int(input("How long did you take: "))

while timetaken != 0:
    if timetaken < 30:
        fast = fast + 1
    elif timetaken < 60:
        medium = medium + 1
    else:
        slow = slow + 1
        
    timetaken = int(input("How long did you take: "))

print(fast, medium, slow)
