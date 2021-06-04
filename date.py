class Date:
	def __init__(self, date_day, date_month, date_year):
		self.date_day = date_day
		self.date_month = date_month
		self.date_year = date_year

	def __repr__(self):
    		return "% s-% s-% s" % (self.date_day, self.date_month, self.date_year) 


# To store number of days in all months from
# January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]

def countLeapYears(date):
	years = date.date_year
	if (date.date_month <= 2):
		years -= 1

	return int(years / 4) - int(years / 100) + int(years / 400)


# This function returns number of days between two
# given dates
def getDifference(date_time1, date_time2):

	numOfDayBeforeDate1 = date_time1.date_year * 365 + date_time1.date_day

	# Add days for months in given date
	for i in range(0, date_time1.date_month - 1):
		numOfDayBeforeDate1 += monthDays[i]

	# Since every leap year is of 366 days,
	# Add a day for every leap year
	numOfDayBeforeDate1 += countLeapYears(date_time1)

	numOfDayBeforeDate2 = date_time2.date_year * 365 + date_time2.date_day
	for i in range(0, date_time2.date_month - 1):
		numOfDayBeforeDate2 += monthDays[i]
	numOfDayBeforeDate2 += countLeapYears(date_time2)

	# return difference between two counts
	return (numOfDayBeforeDate2 - numOfDayBeforeDate1)


# Driver program
date_time1 = Date(1, 1, 1900)
date_time2 = Date(31, 12, 2000)
numOfDays = getDifference(date_time1, date_time2)
if (numOfDays%7) != 0:
	print((numOfDays/7)+1, "-> Number of Monday in between",date_time1,"-",date_time2)
else:
	print((numOfDays/7), "-> Number of Monday")

