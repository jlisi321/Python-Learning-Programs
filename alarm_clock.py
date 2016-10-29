import datetime
import time
import webbrowser

loop = 1

print("Enter Alarm Time: ")
hours = int(input("Hours:"))
minutes = int(input("Minutes:"))
am_pm = input("am/pm:")
url = input("Enter the URL you want opened on the alarm time:")

if(am_pm == "pm"):
	if(hours >= 1 and hours <= 11):
		hours = hours + 12

while(loop == 1):
	now = datetime.datetime.today()
	if(now.hour == hours):
		if(now.minute == minutes):
			loop = 2

webbrowser.open(url)
