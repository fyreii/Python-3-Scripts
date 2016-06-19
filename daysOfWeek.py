dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
weekLen = len(dayNames)
for d in range(0, weekLen):
    print(str(d) + " " + dayNames[d])
departDay = int(input("Please enter the number of the day you are departing: "))
tripLen = int(input("Please enter the number of days you will be gone: "))
totalDays = departDay + tripLen
# % == modulus, the whole remainder assuming the value of totalDays is evenly divided by 7
retDayNum = totalDays % 7
print("You will return on day " + str(retDayNum), "which is a " + dayNames[retDayNum] + ".")





