import re
i = input('podaj ciąg znaków')
def find(string):
    tab = re.findall("[A-Z]", string)
    result = ''.join(tab)
    return result
print(find(i))