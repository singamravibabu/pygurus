class Product():
    name = "my_product"
    price = 0.0
    discountPercent = 0

# create more objects
p1 = Product()
p2 = Product()
p3 = Product()

print(p1.name)
print(p1.price)
print(p1.discountPercent)

# modify the attributes
p1.name = "Samsung Galaxy S10"
p1.price = 49999.99
p1.discountPercent = 10

# printing the modified attributes
print(p1.name)
print(p1.price)
print(p1.discountPercent)