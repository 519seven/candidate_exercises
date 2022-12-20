#!/usr/bin/env python                                                                                                                                         
                                                                                                                                                              
#   Exercise 10

# # Topic                                                                                                                                                     
# # # Signatures                                                                                                                                                  
#
# # Challenge Level                                                                                                                                           
# # # Expert                                                                                                                                                    
#
# # Description                                                                                                                                               
# # # After creating a lengthy code base you have a function you want
#     to know the details about. Create code that will utilize the 
#     signature module to find out details about your function
#                                                                                                                                                             
# # Your Solutions' Relative Levels:                                                                                                                          
# # # N/A                                                                                                                                                             
# 
# # Example Use Case(s)
# # # N/A                                                                                                                                                             
#
# *******************************************************************

from inspect import signature


# Sample function that exists somewhere
def gfg(x:str, y:int):
	pass

# Create signature of callable object
sig = "?"

# Print the signature of the function
print()

# Print the value type of the parameter 'x'
print()

# Print the value type of the parameter 'y'
print(sig.parameters['y'])

# Print the annotation (object type) of the parameter 'y'
print()

