#!/usr/bin/env python

#   Exercise 11

# # Topic
# ## Performance

# # Challenge Level
# ## Medium

# # Description
# 
# # Use bash's `time` command to time this piece of code and compare
#   it to the "sister" code in exercise11_b_loop_v_union.py. Explain
#   any performance differences you may see

# # Your Solutions' Relative Levels:
# # # N/A
#
# # Example Use Case(s)
# # # N/A
#
# *******************************************************************

from modules.test_lists import list_a, list_b

overlaps = set(list_a) & set(list_b)

print(overlaps)

