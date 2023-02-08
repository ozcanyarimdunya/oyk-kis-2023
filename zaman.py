from datetime import datetime

print(datetime.now().year)

n = datetime.now().date().year

now = datetime.now()
now_date = now.date()
now_time = now.time()
print(now_time.microsecond)
print(f"date is {now_date}")
print(f"time is {now_time}")
print(type(now_date))

now_year = now_date.year
print(now_year, type(now_year))

print(now_date.year, now_date.month, now_date.day)
