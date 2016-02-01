import time

current = time.time()

days = current // (24 * 60 * 60)
current = current % (24 * 60 * 60)

hours = current // (60 * 60)
current = current % (60 * 60)

minutes = current // (60)

seconds = current % (60)

print("Days: " + str(days) + "\n" +
	  "Hours: " + str(hours) + "\n" +
	  "Minutes: " + str(minutes) + "\n" +
	  "Seconds: " + str(seconds))

#1437746094.5735958
# % 60 for seconds
# // 60 for minutes
# // (60 * 60) for hours
# // (24 * 60 * 60) for days