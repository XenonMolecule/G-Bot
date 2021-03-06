import re

def altcaps(string):
    matches = re.finditer('[^a-zA-Z]', string)
    sp_chars = []
    sp_char_indices = []
    for m in matches:
        sp_chars.append(m.group(0))
        sp_char_indices.append(m.start())
    new_string = re.sub('[^a-zA-Z]','', string)

    cap_string = [new_string[i] for i in range(len(new_string)) if i%2 == 0]
    low_string = [new_string[i] for i in range(len(new_string)) if i%2 == 1]

    cap_string = list((''.join(cap_string)).upper())
    low_string = list((''.join(low_string)).lower())

    final_string = ""
    last_caps = False
    for i in range(len(string)):
        if(i in sp_char_indices):
            final_string += sp_chars.pop(0)
        elif(not last_caps):
            final_string += cap_string.pop(0)
            last_caps = True
        else:
            final_string += low_string.pop(0)
            last_caps = False
    return final_string


print(altcaps("E:::E"))
