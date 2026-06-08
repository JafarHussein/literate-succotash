import datetime

date=datetime.date(2025,12,24)
print(date)

#Getting todays object

today_date=datetime.date.today()
print(today_date)

#Working with time
time=datetime.time(12,30,00)
print(time)

now=datetime.datetime.now()
now=now.strftime("%H:%M:%S")
print(now)

target_date= datetime.datetime(2050,4,1,21,30,15)
current_date=datetime.datetime.now()

if target_date < current_date:
    print(f"We already passed {target_date}")
else:
    print(f"We still haven't passed {target_date}")
    
