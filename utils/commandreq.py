import collections

class CommandRequest(object):
    def __init__(self, message):
        self.type, self.params = self.parse_message(message)

    # Thank you: @Christian from Stack Overflow -- https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists/2158532#2158532
    def flatten_list(self, l):
        for el in l:
            if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
                yield from self.flatten_list(el)
            else:
                yield el

    # Recursively find strings in list to bond back together using the ending escape characters
    def recursive_remove_escape_chars(self, char, split_char, search_list, length):
        # If the line ends in the escape characters and isn't the end of the list
        #  Utilizes short circuiting
        if((not len(search_list) <= 1) and (search_list[0][(-1 * len(char)):] == char)):
            search_list[0] = search_list[0][:(-1 * len(char))] # Remove the escape character
            search_list[0] += split_char # Add the character back that was split off
            # Attach to the rest of the list that has escape characters
            output = self.recursive_remove_escape_chars(char, split_char, search_list[1:], length+1)
            return search_list[0] + output[0], output[1]
        # No escape char, or at list's end -- just return the current string
        if(len(search_list) > 0):
            return search_list[0], length
        else:
            return "", length

    def splt_with_escp_chars(self, input_string, splt_char, escp_char):
        msg_splt = input_string.split(splt_char)
        delete_indices = []
        skp_len = 0
        for i in range(len(msg_splt)):
            # Ensure no repeats after escape character combines
            if(skp_len > 0):
                delete_indices.append(i)
                skp_len -= 1
                continue
            # Unsplit parts with escape characters
            msg_splt[i], skp_len = self.recursive_remove_escape_chars(escp_char, splt_char, msg_splt[i:], 0)
        for i in range(len(delete_indices)):
            msg_splt.pop(delete_indices[i])
            for j in range(len(delete_indices)):
                delete_indices[j] -= 1
        return msg_splt


    def parse_message(self, message):
        # Get type (First word until space)
        type = ""
        if(len(message) > 1):
            type = message[1:].split(" ")[0]

        # Remove type part
        message = message[len(type)+2:]

        # Process Quote Blocks
        msg_splt = self.splt_with_escp_chars(message, '"', "\\")

        # Every other section should be split by spaces (every other because quote split)
        spce_split_indices = [x for x in range(len(msg_splt)) if x%2 == 0]
        for i in spce_split_indices:
            msg_splt[i] = self.splt_with_escp_chars(msg_splt[i], " ", "\\")

        params = []
        for x in self.flatten_list(msg_splt):
            if(not x == ""):
                params.append(x)

        return type, params
