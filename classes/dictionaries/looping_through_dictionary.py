country_codes = {
    "IN":"India", "US":"United States", "UK":"United Kingdom",
    "AU":"Australia", "JP":"Japan", "SP":"Singapore",
    "CA":"Canada", "MX":"Mexico", "UAE":"United Arabs",
    "NZ":"Newzealand"
}

# use 'for' statement to loop through only keys
for x in country_codes:
    print(x, end=" ")

print() 
# use keys() method to loop through only keys
for x in country_codes.keys():
    print(x, end=" ")

print()
# use values() method to loop through values
for x in country_codes.values():
    print(x, end=" ")

print()

# use items() method to print each key/value pair as a tuple.
for x in country_codes.items():
    print(x)