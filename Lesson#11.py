# LESSON # 11 The Math & Date Time Calender

print ("-----Task 1: Use of math Module-----")
print()
import math

# Task 1.1: Calculate square root
print("Square root of 49 is:", math.sqrt(49))

# Task 1.2: Find the value of pi
print("Value of pi:", math.pi)

# Task 1.3: Calculate factorial of 5
print("Factorial of 5 is:", math.factorial(5))

# Task 1.4: Use ceil and floor
print("Ceil of 7.2 is:", math.ceil(7.2))
print("Floor of 7.8 is:", math.floor(7.8))



print()

print("-----Task 2: Use of datetime Module-----")

print()
import datetime

# Task 2.1: Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Task 2.2: Extract specific parts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)

# Task 2.3: Create a custom date
my_birthday = datetime.date(2000, 5, 15)
print("My birthday is on:", my_birthday)

# Task 2.4: Difference between dates
today = datetime.date.today()
delta = today - my_birthday
print("Days since my birthday:", delta.days)


print()

print ("-----Task 3: Use of calendar Module-----")
print()

import calendar

# Task 3.1: Print calendar for a specific month
print("Calendar for April 2025:")
print(calendar.month(2025, 4))

# Task 3.2: Check if a year is leap
year = 2024
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Task 3.3: Print full year calendar
print("Full year calendar for 2025:")
print(calendar.calendar(2025))
