def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1/num2

print("""Please enter your choice
1) add
2) subtract
3) multiply
4) divide""")

choice = int(input())

num1 = int(input("what is your first num: "))
num2 = int(input("what is your second num: "))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(sub(num1, num2))
elif choice == 3:
    print(mult(num1, num2))
elif choice == 4:
    print(div(num1, num2))
else:
    print("invalid input")