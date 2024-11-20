# String slicing
# index numbers of characters can be used to slice strings
# Syntax for slicing: string[start:end:step]

str = "Hello, World!"
print(str[0:5])     # Hello
print(str[:5])      # Hello
print(str[7:12])    # World
print(str[::2])     # Hlo ol!
print(str[1::2])    # el,Wrd
print(str[::-1])    # !dlroW ,olleH
print(str[::3])     # Hl r!