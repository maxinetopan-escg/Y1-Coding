Astar = 95
A = 90
B = 80
C = 70
D = 60
E = 50

def getGrade(grade):
    if grade >= Astar:
        return "A*"
    elif grade > A:
        return "A"
    elif grade > B:
        return "B"
    elif grade > C:
        return "C"
    else:
        return "No Grade"

complete = False
while complete == False:
    try:
        grade = int(input("please enter your grade: "))
        result = getGrade(grade)
        print(result)  
        complete = True
    except:
        print("You got an error :( probably an invalid value")
