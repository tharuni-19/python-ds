with open("DAY-10\merge1.txt") as f1,open("DAY-10\merge1.txt") as f2:
    text=f1.read() + f2.read()
with open("Day-10/mergedText.txt","w") as f:
    f.write(text)