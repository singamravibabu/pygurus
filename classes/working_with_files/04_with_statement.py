# To avoid using close() method explicitly
# Use the 'with' statement to create a context
# Once the context ends all the opereations in the context also end
# including files

with open("sample.txt", "r") as f:
    print(f.read())
