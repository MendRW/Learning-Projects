#Matching and extracting Data
# re.search() returns a T/F depending on whether the string matches the regular expression
# if we actually want the matching strings to be extracted we use re.findall()
## TLDR re.search() tells you if it exists (true or flase)
## TLDR re.findall() will return the matching strings in a list

import re
# import re (regular expression or regex)
x = 'my 2 favorite numbers are 19 and 42 AA'
# x variable is the text we are executing the re.findall on
y =  re.findall ('[0-9]+',x)
# setting y to the result of re.findall under the condition of 0-9
print (y)
# tell me y in a list

y = re.findall('[AEIOU]+',x)
# This is the same but is searching for AEIOU the + tells it to search for duplicates e.g AA EE II OO UU within x
print (y)
## this will return a list of the characters that match e.g AA

## Greedy Matching = Always picks the larger/longer of the two string options
## To disable greedy matching add a ? e.g ^F.+?:
## ^ (first character) ^F (first character is an F) ^F.+? (One or more characters but not greedy) : last character in the match is a :
## This means it will match with: First character being F until it finds a : and then stops looking