# span of time - timedelta
# from datetime module use the timedelta to construct time span
# Syntax:
# timedelta([days][, seconds][, microseconds][, milliseconds][, minutes][, hours][, weeks])

from datetime import date, time, datetime, timedelta

us_trip = timedelta(weeks=20)
report_duration = timedelta(hours=4)
home_trip = timedelta(weeks=2, days=3, hours=12, minutes=5)

print(us_trip)
print(report_duration)
print(home_trip)

start_date = datetime(2024, 12, 2, 10, 30)
return_date_time = start_date + us_trip
print(f"Return date and time: {return_date_time}")

their_start_date = datetime.now() - us_trip
print(their_start_date)