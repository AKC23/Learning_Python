#
# Example file for working with Calendars
#

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2021, 6, 0, 0)
print("Calendar will look like this:")
print(str)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
print("HTML formatted calendar will look like this:")
str = hc.formatmonth(2021, 6)
print(str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021, 6):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("\nName of the months in calendar")
for name in calendar.month_name:
    print(name)

print("\nName of the days in a week")
for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1, 13):
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(2021, m)
    # The first Friday has to be within the first two weeks
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
      # if the friday value of the first week isn't zero then there is a friday in that week
        meetday = weekone[calendar.FRIDAY]
    else:
        # if the first friday isn't in the first week, it must be in the second week
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
