import datetime
x = datetime.datetime.now()
y = datetime.timedelta(days=5)
data = x - y
five_days_before = data.strftime("%Y/%m/%d")
print(five_days_before)