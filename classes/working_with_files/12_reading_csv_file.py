import csv

with open("books.csv", "r", newline="") as file:
    r_obj = csv.reader(file)
    for line in r_obj:
        print(line)