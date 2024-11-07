# Opening a File in read mode
# open("./sample.txt", "r")     # ./ means current directory
# open("../sample.txt", "r")    # ../ means parent directory
# open("D:\\pygurus\\classes\\working_with_files\\sample.txt", "r")
# open("notes2023.txt", "r")     # we can't read file that doesn't exists
f = open("./sample.txt", "r")
print(f.read())
f.close()

