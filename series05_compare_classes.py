#!/usr/bin/env python

#   Series 5

# # Topic
# # # Comparing Classes
# # Challenge Level
# # # Medium
# # Description
# # # Check if two objects contain the same values in each of their variables by overriding `==`
#
# # Your Solutions' Relative Levels:
# # # - N/A
#
## Example Use Cases(s)
#
#    class1 = MyClass('hello')
#    class2 = MyClass('goodbye')
#    class3 = OtherClass('hello')
#    class4 = MyClass('hello')
#
#  class1 DOES NOT have the same values as class2
#  class2 DOES NOT have the same values as class3
#  class3 DOES NOT have the same values as class4
#  class1 DOES have the same values as class4
#
# *******************************************************************

class ImportantClass:

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class OtherClass:

    def __init__(self):
        self.is_different = True

myclass1 = ImportantClass('field', 'stream')
myclass2 = ImportantClass('meadow', 'plain')
myclass3 = ImportantClass('meadow', 'plain')
myclass4 = OtherClass()
