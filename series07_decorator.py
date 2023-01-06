#!/usr/bin/env python

#   Series 7

# # Topic
# # # Decorators
# # Challenge Level
# # # Medium
# # Description
# # # Describe how the code below illustrates the use of a decorator
#     Or, write your own.
#
# # Your Solutions' Relative Levels:
# # # - N/A
#
## Example Use Cases(s)
# # # - N/A
#
# *******************************************************************

def my_decorator(func):
    def inner():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return inner

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
