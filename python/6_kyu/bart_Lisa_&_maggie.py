# Instructions

# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''

# Solution

def namelist(names):
    ls = [i['name'] for i in names]
    
    if len(ls) > 1:
        result = (f"{', '.join(ls[0:-1])}" + f" & {ls[-1]}")
    elif len(ls) == 1:
        result = ls[0]
    else:
        result = ''

    return result
  
  
#   Tests

# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
# "Must work with many names")
# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
# "Must work with many names")
# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
# "Must work with two names")
# test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
# test.assert_equals(namelist([]), '', "Must work with no names")
