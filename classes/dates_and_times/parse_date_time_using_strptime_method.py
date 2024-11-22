# strptime method is from datetime construct
# strptime: 'p' parse (get)
# %d - day number of a month
# %m - month number
# %y - 2-digit year number
# %Y - 4-digit year number
# %H - hour
# %M - minute
# %S - second

from datetime import datetime

dt1 = "2024-11-22"
dt2 = "22/11/2024"
dt3 = "11-22/2024"
dt4 = "25th of 11th month in the year 2024."
dt5 = "I was there 10 o'clock 30 minute, on 2/28/2023"

d1 = datetime.strptime(dt1, "%Y-%m-%d")
d2 = datetime.strptime(dt2, "%d/%m/%Y")
d3 = datetime.strptime(dt3, "%m-%d/%Y")
d4 = datetime.strptime(dt4, "%dth of %mth month in the year %Y.")
d5 = datetime.strptime(dt5, "I was there %H o'clock %M minute, on %m/%d/%Y")

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
