number = 123456.7890123

# width
print("{:25}".format(number))
print("{:35}".format(number))
print("{:<45}".format(number))

# with and comma
print("{:25,}".format(number))
print("{:35,}".format(number))
print("{:45,}".format(number))

# width, comma and deci_places
print("{:25,.2f}".format(number))
print("{:35,.3f}".format(number))
print("{:45,.4f}".format(number))

value1 = 0.35
# percent
print("{:25,.2%}".format(value1))
