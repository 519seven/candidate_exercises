#!/usr/bin/env python

#   Exercise 4
# # Topic
# # # Lists and Imported Package
# # Challenge Level
# # # Medium
# # Description
# # # Given an array (list) of lists, return True if the array has
#     two of the same values together.
#
# # Your Solutions' Relative Levels:
#
# - *Easy/Beginner*: `if`/`else`
# - *Medium/Intermediate*: `pairwise` package
# - *Hard/Expert*: zip and shift
#
# # Example Use Case(s)
#
#   `['apple', 'apple', 'banana', 'orange']` 
#   DOES meet the condition
# 
#   `['apple', 'banana', 'orange', 'grape']`
#   DOES NOT meet the condition
#
#   `['apple', 'pear', 'banana', 'orange', '2', '2']`
#   DOES meet the condition
#
# ********************************************************************

from more_itertools import pairwise # (optional)

def has_same(my_list):
  pass

list1 = ['apple', 'apple', 'banana', 'orange']
list2 = ['apple', 'banana', 'orange', 'grape']
list3 = ['apple', 'pear', 'banana', 'orange', '2', '2']
array_of_lists = [list1, list2, list3]
print(array_of_lists)
