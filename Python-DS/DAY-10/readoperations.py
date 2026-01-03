with open("DAY-10/file.txt", "r") as f:
    readOperation = f.read()
    print(readOperation)

with open("DAY-10/file.txt", "r") as f:
    readlineOperation = f.readline()
    print(readlineOperation)

with open("DAY-10/file.txt", "r") as f:
    readlinesOperation = f.readlines()
    print(readlinesOperation)
