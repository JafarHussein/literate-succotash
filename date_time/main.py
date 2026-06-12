import datetime

date=datetime.date(2025,1,13)

print(f"Today's date is {date}")

#Getting the date right now

today_date=datetime.date.today()
print(today_date)

#Working with time
time=datetime.time(12,30,0)
print(time)

current_time=datetime.datetime.now()
current_time=current_time.strftime("%H:%M:%S")
print(f"The current time is {current_time}")