from datetime import date, time, datetime, timedelta

project_duration = timedelta(weeks=3, days=4, hours=5, minutes=28, seconds=45)

# attributes and method of timedelta return in: days, seconds and microseconds

# days - returns number of days
print(project_duration.days)

# seconds - returns number of seconds in addtion to days
print(project_duration.seconds)

# microseconds - returns microseconds in addtion to days and seconds
print(project_duration.microseconds)

# total_seconds() - total number of seconds and microseconds
print(project_duration.total_seconds())