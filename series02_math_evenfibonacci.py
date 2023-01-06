#!/usr/bin/env python
from fibonacci import fibonacci

#   Series 2

# # Topic
# ## Math

# # Challenge Level
# ## Easy

# # Description
#
# # ProjectEuler.com Problem 2 
#   Find the sum of all the even Fibonacci numbers that are less than 4 million.
#   Fibonacci explained: https://www.calculatorsoup.com/calculators/discretemathematics/fibonacci-calculator.php
#
# # Your Solutions' Relative Levels:
#   Easyu: while loop
#   Intermediate: using py-fibonacci (https://pypi.org/project/py-fibonacci/)
#   Hard: create your own library
#
# # Example Use Case(s)
#
# - A Fibonacci sequence involves adding the previous number to the current 
#   number.  In this exercise, we are starting with 0 and 1.
#   Example: 0 1 1 2 3 5 8 13 21 34 55 89
# ******************************************************************************

# initialize variables
MAX_NUM = 4e6          # 4000000
CUMULATIVE_SUM = 0     # track the sum of even numbers

a, b = 0, 1

# add your solution to update CUMULATIVE_SUM

if CUMULATIVE_SUM > 0:
    print(f"The sum of numbers of a Fibonacci sequence that are even and less than {int(MAX_NUM)} is {CUMULATIVE_SUM}")
print("The End.")

import sys
sys.exit(0)
