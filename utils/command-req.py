class CommandRequest(object):
    def __init__(self, message):
        pass #self.type, self.params = self.parse_message(message)

    # Recursively find strings in list to bond back together using the ending escape characters
    def recursive_remove_escape_chars(self, char, split_char, search_list, length):
        print(search_list)
        # If the line ends in the escape characters and isn't the end of the list
        #  Utilizes short circuiting
        if(not len(search_list) <= 1 and search_list[0][(-1 * len(char)):] == char):
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



    def parse_message(self, message):
        # Get type (First word until space)
        type = ""
        if(len(message) > 1):
            type = message[1:].split(" ")[0]

        # Remove type part
        message = message[len(type):]

        # Process Quote Blocks
        quote_splt = message.split('"')
        skp_len = 0
        for i in range(len(quote_splt)):
            if(skp_len > 0):
                quote_splt[i] = 0
                skp_len -= 1
            # Escape Characters - Must Unsplit
            if(quote_splt[i][-1:] == "\\" and not i == new_len-1):
                quote_splt[i] = quote_splt[i][0:-1]
                quote_splt[i] += '"' + quote_splt[i+1]
                new_len -= 1

test = CommandRequest("")
print(test.recursive_remove_escape_chars("\\", '"', '\\"Hello World\\"\\'.split('"'), 0))
print(test.recursive_remove_escape_chars("\\", '"', [], 0))
