import datetime
day1 = datetime.date(2022, 10, 15)
day1

day2 = datetime.datetime(2022, 10, 15, 16, 10, 30)
day2.year
day2.month
day2.day
day2.hour
day2.minute
day2.second

datetime.date.today()
datetime.datetime.now()

day1 = datetime.date(2022, 10, 15)
day2 = datetime.date(2022, 11, 10)

diff = day2 - day1
print(diff)