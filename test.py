import re

def oob(string):
    b_conflicts = re.findall('[aeiouy]b',string)
    for b in b_conflicts:
        print(b)
        string = string.replace(b, b[0])
        print(string)
    new_string = re.sub('[aeiouy]','oob',string)
    new_string = re.sub('[AEIOUY]','Oob',new_string)
    return new_string
