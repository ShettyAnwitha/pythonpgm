from dateutil.relativedelta import relativedelta
from datetime import datetime

date_time=datetime.today()
print("Current date :",date_time)

print("remaining days for new year")
dateandtime=datetime(date_time.year+1,1,1,0,0,0) 
time=relativedelta(dateandtime,date_time) 

print("remaining years:", time.years, ", remaining months:",time.months, "remaining days:",time.days,",remaining hours :",time.hours,",minutes left:",time.minutes,
      ",seconds left:",time.seconds)
