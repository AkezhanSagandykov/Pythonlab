import datetime
day = int(input())
x = datetime.datetime.now()
y = datetime.timedelta(days = day)
two_dates = x - y
difference = (x - two_dates).total_seconds()
print(difference)