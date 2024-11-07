# READ METHODS
# read() - reads entire files as one text string
# readlines() - returns an list, where each line is an item in the list
# readline() - reads the next line

# The read() to read entire file as one single string
with open("courses.txt", "r") as file:
    print(file.read())