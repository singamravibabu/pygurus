from datetime import date, time, datetime, timedelta

this_day = date.today()

future_date = date(2024, 12, 5)
past_date = date(2024, 10, 15)

print(this_day > past_date)
print(this_day > future_date)
print(past_date < future_date)