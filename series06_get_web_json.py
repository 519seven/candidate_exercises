#!/usr/bin/env python

#   Series 6

# # Topic
# # # Basic web GET and JSON processing
# # Challenge Level
# # # Medium
# # Description
# # # Given a URL (no authentication required), print out a list of 
#     years that are present in the data returned.
#
# # Your Solutions' Relative Levels:
#
# - *Easy/Beginner*: `if`/`else`
# - *Medium/Intermediate*: list comprehension
# - *Hard/Expert*: lambda
#
# # Example Use Case(s)
# 
#   Given that URL is equal to https://datausa.io/api/data?drilldowns=Nation&measures=Population, this list of the years returned is:
# 
#   `['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']`
# 
# *******************************************************************

import urllib
import json

URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
HEADERS = {'User-Agent' : "Manual Testing - Not a bot"}

def get_web_data(url):
    req = urllib.request.Request(url, headers=HEADERS) 
    con = urllib.request.urlopen( req )
    return con.read()

my_data = get_web_data(URL)
# get third list
third_list = my_data["data"][2]

