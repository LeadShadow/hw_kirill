'''
Метод: sub
'''

import re

string = "The best language is Java"

# заменить слово Java на Python


new_string = re.sub('Java', 'Python', string)
print(new_string)
