a = 42   # first number
b = 14   # second number

while a != b:
    if a > b:
        a -= b  # subtract b from a if a is greater
    else:
        b -= a  # subtract a from b if b is greater

print(a)