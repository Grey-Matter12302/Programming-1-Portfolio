import datetime

now = datetime.datetime.now()
timeInput = input('Enter your birthday in YYYY/MM/DD format please:')

if (len(timeInput) == 10):
    bDay = timeInput[8:9]
    bMonth = timeInput[5:6]
    bYear = timeInput[0:4]
    dayAge = now.day - int(bDay)
    monthAge = now.month - int(bMonth)
    yearAge = now.year - int(bYear)
    timeDifference = (yearAge * 365 + monthAge * 30.4 + dayAge)
    finalYearAge = int(timeDifference/365)
    finalMonthAge = int((timeDifference - finalYearAge * 365) -((timeDifference - finalYearAge*365)%30.4))/30.4
    finalDayAge = int(timeDifference - finalYearAge*365 - finalMonthAge*30.4)
    print('You are ' + str(finalYearAge) + ' years, ' + str(finalMonthAge) + ' months and ' + str(finalDayAge) + ' days old')
else:
    print ("You didn't input the date in the right format. Try Again.")
