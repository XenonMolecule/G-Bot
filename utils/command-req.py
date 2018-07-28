class CommandRequest(object):
    def __init__(self, message):
        pass #self.type, self.params = self.parse_message(message)

    def recursive_remove_escape_chars(self, char, split_char, search_list, length):
        if(search_list[0][(-1 * len(char)):] == char and not length == len(search_list)-1):
            search_list[0] += split_char
            output = self.recursive_remove_escape_chars(char, split_char, search_list[1:], length+1)
            return search_list[0] + output[0], output[1]
        if(search_list[0][(-1 * len(char)):] == char):
            search_list[0] = search_list[:(-1 * len(char))]
            search_list[0] += split_char
        return search_list[0], length


    def parse_message(self, message):
        # Get type (First word until space)
        type = ""
        if(len(message) > 1):
            type = message[1:].split(" ")[0]

        # Remove type part
        message = message[len(type):]

        # Process Quote Blocks
        quote_splt = message.split('"')
        new_len = len(quote_splt)
        for i in range(len(quote_splt)):
            # Escape Characters - Must Unsplit
            if(quote_splt[i][-1:] == "\\" and not i == new_len-1):
                quote_splt[i] = quote_splt[i][0:-1]
                quote_splt[i] += '"' + quote_splt[i+1]
                new_len -= 1

test = CommandRequest("")
print(test.recursive_remove_escape_chars("\\", '"', '\\"Hello World\\"'.split('"'), 0))
