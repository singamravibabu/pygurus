# strftime() method from datatime module helps us to format datetime objects
# 'f' in strftime() stands for fromat
# format codes:
# %a    - Abbreviated weekday (Sun, Mon, Tue, ...)
# %A    - Full weekday (Sunday, Monday, Tuesday, ...)
# %b    - Abbreviated month (Jan, Feb, Mar, ...)
# %B    - Full month (January, February, March, ...)
# %d    - Zero-padded day of month (01, 02, 03, ..., 11, ...25, ..., 31)
# %m    - Zero-padded month as a number (01, 02, ..., 10, 11, 12)
# %Y    - Four-digit year number (2014, 2024, etc.)
# %y    - 2-digit year number (14, 24, etc.)
# %H    - 24-hour format (0-23)
# %I    - 12-hour format
# %M    - Minute format
# %S    - Second format
# %p    - AM/PM specifier
# %f    - microsecond specifier

from datetime import datetime

sample_dt = datetime(2024, 11, 30, 10, 32, 45)

print(sample_dt)
print(sample_dt.strftime("%A - %b %d, %Y"))
print(sample_dt.strftime("%Y-%m-%d (%A)"))
print(sample_dt.strftime("%B %d (%a), %Y"))
print(sample_dt.strftime("%A (%B %d %Y)"))
