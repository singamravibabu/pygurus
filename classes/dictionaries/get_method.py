country_codes = {
    "IN":"India", "US":"United States", "UK":"United Kingdom",
    "AU":"Australia", "JP":"Japan", "SP":"Singapore"
}

in_key = country_codes.get("IN")
print(in_key)

# if the key isn't in the dictionary, get() returns None
am_key = country_codes.get("AM")
print(am_key)

# in the 2nd parameter of the get() method specify what to return when a key doesn't exists
pm_key = country_codes.get("PM", "Key Not Found")
print(pm_key)