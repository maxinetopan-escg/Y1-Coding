origText = input("please enter your text to compress: ")

compressedText = ""
prevC = None
repeatCount = 1

for c in origText:
    if c == prevC:
        repeatCount += 1
    elif prevC:
        compressedText += f"{prevC} {repeatCount} "
        repeatCount = 1
    prevC = c

compressedText += f"{origText[-1]} {repeatCount}"

print(compressedText)