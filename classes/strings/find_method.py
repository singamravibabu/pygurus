# find(substring[, start][, end])

email = "anil.kumar@gmail.com"

at_index = email.find("@")
print(at_index)     # 10

dot_index = email.find(".", email.find("@")+1)
print(dot_index)    # 16
