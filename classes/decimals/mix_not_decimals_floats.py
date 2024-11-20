from decimal import Decimal

value = Decimal("10.01")

# Legal: add Decimal and an integer
print(value + 100)

# Illegal: combine Decimal and float
print(value + 10.1)