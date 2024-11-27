country_codes = {
    "IN":"India", "US":"United States", "UK":"United Kingdom",
    "AU":"Australia", "JP":"Japan", "SP":"Singapore",
    "CA":"Canada", "MX":"Mexico", "UAE":"United Arabs",
    "NZ":"Newzealand"
}
print(country_codes)

# del keyword: to delete an item specifying its key
del country_codes["NZ"]
print(country_codes)

# pop() method: pop(key[, default_value])
# pop() returns the value then deletes it
print(country_codes.pop("UAE"))
print(country_codes)

# clear() method deletes all items from a dictionary
country_codes.clear()
print(country_codes)
