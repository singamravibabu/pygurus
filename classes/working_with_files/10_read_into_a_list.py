depts_list = []
with open("departments.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        depts_list.append(line)

print(depts_list)