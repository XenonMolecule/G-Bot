import re

def altcaps(string):
    space_indices = [m.start() for m in re.finditer(' ', string)]
    new_string = re.sub(' ','', string)

    cap_string = [new_string[i] for i in range(len(new_string)) if i%2 == 0]
    low_string = [new_string[i] for i in range(len(new_string)) if i%2 == 1]

    cap_string = list((''.join(cap_string)).upper())
    low_string = list((''.join(low_string)).lower())

    final_string = ""
    last_caps = False
    for i in range(len(string)):
        if(i in space_indices):
            final_string += " "
        elif(not last_caps):
            final_string += cap_string.pop(0)
            last_caps = True
        else:
            final_string += low_string.pop(0)
            last_caps = False
    return final_string


print(altcaps("test number two and now test number three"))
