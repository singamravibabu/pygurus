country_codes = {
    "IN":"India", "US":"United States", "UK":"United Kingdom",
    "AU":"Australia", "JP":"Japan", "SP":"Singapore"
}

# Syntax: key in dictionary
print("IN" in country_codes)        # True
print("AM" in country_codes)        # False

if "IN" in country_codes:
    print(country_codes["IN"])      # India
    
if "AM" in country_codes:
    print(country_codes["AM"])      # doesn't print this
else:
    print("No key named: AM")      # prints this