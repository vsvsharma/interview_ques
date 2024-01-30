"""
Problems URL(https://www.hackerrank.com/challenges/calendar-module/problem)
"""

from datetime import datetime

def find_day(month, day, year):
    # Parse the input date
    input_date = f"{month} {day} {year}"
    date_object = datetime.strptime(input_date, '%m %d %Y')

    # Get the day name and print in uppercase
    day_name = date_object.strftime('%A').upper()
    print(day_name)


input_date = input()
month, day, year = map(int, input_date.split())
find_day(month, day, year)
