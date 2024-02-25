import datetime
current_date = datetime.datetime.now()
current_dates = datetime.timedelta(days=1)
today = current_date.strftime("%Y/%m/%d")
x = current_date+current_dates
y = current_date-current_dates
tomorrow = x.strftime("%Y/%m/%d")
yesterday = y.strftime("%Y/%m/%d")
print(yesterday)
print(today)
print(tomorrow)