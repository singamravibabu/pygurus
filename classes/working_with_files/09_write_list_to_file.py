depts = ["it", "sales", "hr", "admin", "marketing",
         "accounts", "finance"]
with open("departments.txt", "w") as file:
    for d in depts:
        file.write(d + "\n")
