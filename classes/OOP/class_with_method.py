class Product():
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def discountAmount(self):
        return (self.price * self.discountPercent) / 100

    def discountPrice(self):
        return self.price - self.discountAmount()

p1 = Product("Phone", 34000.0, 5)

# printing the attributes of the object
print(p1.name)
print(p1.price)
print(p1.discountPercent)

# printing the discount amount and discounted price
print(p1.discountAmount())
print(p1.discountPrice())