timeSleep  = int(input())
timeHour   = int(input())
timeMinute = int(input())

hours 	= timeSleep // 60
minutes = timeSleep - hours * 60

resultHours   = timeHour + hours
resultMinutes = timeMinute + minutes

if resultMinutes > 59:
	resultMinutes -= 60
	resultHours   += 1

print(resultHours)
print(resultMinutes)