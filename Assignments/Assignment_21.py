# Write a python program to generate and display the next date of a given date.
#
# Assume that
# Date is provided as day, month and year as shown in below table.
# The input provided is always valid. Output should be day-month-year.
# Hint: print(day,"-",month,"-",year) will display day-month-year
#
# Sample Input	Expected Output
# Day	1	2-9-2015
# Month	9
# Year	2015
#
# Also identify the test data and use it to test the program.


#Solution:

# PF-Tryout

def generate_next_date(day, month, year):
    # Start writing your code here
    leap_yr = False
    if ((year % 400 == 0) and (year % 4 == 0)):
        leap_yr = True
    elif (year % 100 == 0):
        leap_yr = False
    else:
        leap_yr = False

    if (month == 1, 3, 5, 7, 8, 10, 12):
        month_days = 31
    elif (month == 2):
        if leap_yr:
            month_days = 29
        else:
            month_days = 28
    else:
        month_days = 30

    if day < month_days:
        day = day + 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    next_day = day
    next_month = month
    next_year = year

    print(next_day, "-", next_month, "-", next_year)

generate_next_date(6, 8, 2020)