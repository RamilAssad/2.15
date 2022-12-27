filterptr = open("file2.txt", "r")
content = filterptr.read()
print(type(content))
print(content)
filterptr.close()

with open("file3.txt", "r") as fileptr:
    content = fileptr.read(20)
    print(type(content))
    print(content)


fileptr = open("file3.txt", "r")
for i in fileptr:
    print(i)
fileptr.close()