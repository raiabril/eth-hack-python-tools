#!/usr/bin/env python3

"""
ASCII parser

This script receives a string representing ASCII characters and returns the corresponding string representation in UTF-8.

"""

# Initialising list
int_list = [int(x) for x in input("Input the list of ASCII characters: ").split(" ")]
  
# Using map and join
res = ''.join(map(chr, int_list))
  
# Print the resultant string
print ("Resultant string: ", str(res))