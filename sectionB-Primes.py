loop = "y"

while loop == "y":
    num = int(input("Please enter a positive integer: "))

    if (num <= 1):
        print("Not greater than 1")
    else:
        prime = True
        for i in range(num - 1, 1, -1):
            #print(f"{num} / {i} = {num/i}: {(num/i) % 1 == 0}")
            if (num/i) % 1 == 0:
                prime = False
                break

        if prime:
            print("Is prime")
        else:
            print("Is not prime")
    
    loop = input("enter another number? (y/n): ").lower()