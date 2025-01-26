

'''
re.findall():
The re.findall() method returns a list of strings containing all matches.
If the pattern is not found, re.findall() returns an empty list.
'''

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)



'''
re.split():
The re.split method splits the string where there is a match and returns a list 
of strings where the splits have occurred.
If the pattern is not found, re.split() returns a list containing the original string.
'''

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)
'''
You can pass maxsplit argument to the re.split() method. It's the maximum number of splits 
that will occur.
'''
string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)
'''
By the way, the default value of maxsplit is 0; meaning all possible splits.
'''