#!/usr/bin/python3
def complex_delete(a_dictionary, value):
   bounce = a_dictionary.copy()
   for k, v in bounce.items():
      if v == value:
         del a_dictionary[k]
   return a_dictionary
