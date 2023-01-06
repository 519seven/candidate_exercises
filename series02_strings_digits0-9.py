#!/usr/bin/env python

#   Series 2

# # Topic
# # # Strings
# # Challenge Level
# # # Medium
# # Description:
# # # There is only one number whose square along with its cubed value
#     contain one and only one of the digits 0-9.Write a snippet that 
#     will find that number.Hint: the exponent operator symbol is `**`
#
# # Your Solutions' Relative Levels:
#
# - *Easy/Beginner*: `if`/`else`
# - *Medium/Intermediate*: list comprehension
# - *Hard/Expert*: lambda
#
# # Bonus Requirements
# 
# - Don't compare all possible numbers if there aren't enough digits to begin with
# - Stop processing after number is found.
#
# # Example Use Case(s)
#
# `X = 23`
#
# The values of `X^2` and `X^3` contains a set of digits
#
# ```
# 23^2 = 529
# 23^3 = 12167
# ```
# 
# Together those two sets of digits are: `11225678`
#
# Pass/Fail? `Fail`

# TL;DR;
# 
# Loop through a bunch of numbers, starting at 0
# Return the one whos square and cube contain
# one and only one of each digits 0-9
#
#

MAX = 1000

def compare(my_string):
  pass

for i in range(0, MAX):
  # get square, convert to string
  digits_of_square = i**2
  digits_of_cube = i**3
  all_digits = str(digits_of_square)+str(digits_of_cube)
  print(f"Checking {all_digits} for all digits...")
  print(f"Our number is: {i}") if compare(all_digits) else ""

