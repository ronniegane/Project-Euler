''' Project Euler problem 19: Counting Sundays
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

# use 0 = Sunday, 1 = Monday.... 6= Saturday
# and mod 7 arithmetic

monthDays = {
    # translates months into days. 1 = January, 12 = December
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }

startDMY = {'day': 1, 'month': 1, 'year': 1900}
startDay = 1 # Jan 1 1900 was a Monday
sundayCount = 0

current = startDMY
day = startDay

while current['year'] < 2001: # run til dec 31, 2000
    # add correct number of days
    # check for leap years
    if current['month'] == 2 and (current['year'] % 400 == 0 or(current['year'] % 4 == 0 and current['year'] % 100 != 0)):
        # add 29 days
        day += 29
    else:
        day += monthDays[current['month']]

    # divide current day modulo 7 to check if it is a sunday
    day = day % 7
    if day == 0 and current['year'] > 1900: # only starting count from Jan 1901
        # add to count
        sundayCount += 1

    # increase the month, and the year if necessary
    current['month'] += 1
    if current['month'] > 12:
        current['year'] += 1
        current['month'] = 1



print("Total number of sundays is %s" % sundayCount)
    

    
