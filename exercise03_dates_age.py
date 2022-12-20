#!/usr/bin/env python

#   Exercise 3
# # Topic
# # # Dates
# # Challenge Level
# # # Easy
# # Description
# # # Ask the end user for their date of birth
#     and calculate their age.
#
# # Your Solutions' Relative Levels:
#
# - *Easy/Beginner*: Simple math
# - *Medium/Intermediate*: Date object
# - *Hard/Expert*: lambda

# # Example Use Case(s)
#
#   User input: `11/07/1990`
#   Age: `32`
# *******************************************************************

import datetime

dob_year = input("What is your year of birth? (YYYY): ")
dob_month = input("What is your month of birth? (MM): ")
dob_day = input("What is your day of birth? (DD): ")

print(f"Your birthday is {dob_month}/{dob_day}/{dob_year}")
