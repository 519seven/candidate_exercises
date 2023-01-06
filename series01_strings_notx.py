#!/usr/bin/env python

#   Series 1

# # Topic
# ## Strings

# # Challenge Level
# ## Easy

# # Description
# 
# # Find the pattern in line 41 in the strings listed in
#   lines 31 through 38.Return result ONLY IF the char-
#   acter immediately preceeding the pattern is NOT "x".

# # Your Solutions' Relative Levels:
#
# - *Easy/Beginner*: `if`/`else`
# - *Medium/Intermediate*: list comprehension
# - *Hard/Expert*: Anonymous (lambda) function
#
# # Example Use Case(s)
#
# The string `easypeasy12x.xyz` DOES NOT meet the conditions
#
# The string `thebrown.dog.xyz` DOES meet the conditions
# 
# The string `senditherex.xyz.ext` DOES NOT meet the conditions
# ******************************************************************************
# Find string with pattern where "x" does not come before pattern
# strings:
#   xyztothest.orex.yz
#   easypeasy12x.xyz
#   dragxyz.to.theleft
#   senditherex.xyz.ext
#   yz.x
#   thebrown.dog.xyz
#   a.xyz
#   thexorangesyarezcrushed
#
# look for:
#   .xyz
# ******************************************************************************
def find_substr(full, sub):
    pass

# create list
mylist = []
pattern = ".xyz"

# check all items in list for substring
find_substr(mylist, pattern)

