fileptr = open("newfile.txt", "x")
print(fileptr)

if fileptr:
    print("file created successfully")

fileptr.close()

with open("newfile2.txt", "x") as fileptr1:
    print(fileptr1)

    if fileptr:
        print("File created successfully")