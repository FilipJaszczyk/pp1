import re
txt = 'To be, or not to be, that is the question'
counter = 0
letters = re.findall(r'o|e|u|a|i',txt)
print(len(letters))