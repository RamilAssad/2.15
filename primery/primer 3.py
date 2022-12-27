fileptr = open("file2.txt", "r")

content1 = fileptr.readline()
content2 = fileptr.readline()

print(content1)
print(content2)

fileptr.close()


with open("file3.txt", "r") as fileptr2:
    content1 = fileptr2.readline()
    content2 = fileptr2.readline()

    print(content1)
    print(content2)