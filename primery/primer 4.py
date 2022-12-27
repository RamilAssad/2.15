fileptr = open("file2.txt", "r")

content = fileptr.readlines()
print(content)

fileptr.close()


with open("file3.txt", "r") as fileptr1:
    content1 = fileptr1.readlines()

    print(content1)