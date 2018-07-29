import re
from utils.command import Command

class Oobify(Command):
    def __init__(self):
        super().__init__("oobify")

    def oob(self, string):
        b_conflicts = re.findall('[aeiouy]b',string)
        for b in b_conflicts:
            string = string.replace(b, b[0])
        new_string = re.sub('[aeiouy]','oob',string)
        new_string = re.sub('[AEIOUY]','Oob',new_string)
        return new_string

    async def run(self, client, message, type, params):
        params = " ".join(params)
        await client.send_message(message.channel, self.oob(params))

    async def help(self, client, message):
        await client.send_message(message.channel, self.name + " usage: `!oobify [string to oobify]`")
