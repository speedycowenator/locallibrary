
from datetime import date
import datetime

date_now = date.today()

def unix(time):
	time = time.isocalendar()
	seconds_year = (time[0] - 1970) * 31556952 
	seconds_week = time[1] * 604800
	seconds_day = time[2] * 86400
	seconds_total = seconds_year + seconds_week + seconds_day
	return seconds_total

def how_old(time):
	time = unix(time)
	time_age_seconds = unix(date_now) - time 
	time_age_days = time_age_seconds/(86400)
	time_age_days = int(round(time_age_days))
	return(time_age_days)

##############################

date_test = datetime.date(2019,8,8)

age = how_old(date_test)

print(age)
