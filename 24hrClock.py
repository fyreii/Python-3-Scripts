currTime = int(input("Enter the current time in 24hr format: "))
alarmTime = int(input("Enter the desired number of hours for alarm: "))
finalTime = (currTime + alarmTime) % 24
print(finalTime)
