# Unlike list and tuples, dictionaries are not sequences
# dictionary has items, where each item is a key/value pair
'''Syntax:
    {key1:value1, key2:value2, key3:value3, key4:value4, ...}
'''

# create dictionary
country_codes = {
    "IN":"India", "US":"United States", "UK":"United Kingdom",
    "AU":"Australia", "JP":"Japan", "SP":"Singapore"
}


# Access values using their respective keys
print(country_codes["IN"])
print(country_codes["US"])
print(country_codes["JP"])

# adding items to a dictionary
country_codes["UAE"] = "United Arab Emirites"
country_codes["CA"] = "Canada"
print(country_codes)

# change value of a key / setting an item
country_codes["JP"] = "Jamaica"

print(country_codes)