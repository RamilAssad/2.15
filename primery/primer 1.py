fileptr = open("file2.txt", "w")

fileptr.write(
    "Python is the modern day language. It makes things so simple.\n"
    "It is the fastest-growing programing language"
)

fileptr.close()

with open("file3.txt", "w") as fileptrr:
    fileptrr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
    )
