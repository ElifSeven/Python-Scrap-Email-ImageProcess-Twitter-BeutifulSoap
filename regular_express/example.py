import re

string = 'search inside of this text please!'
print('search' in string)
print(re.search('of', string))

search_string = 'of' in string
