from utils.command import Command

class GWhat(Command):
    def __init__(self):
        super().__init__("gwhat")

    async def run(self, client, message, type, params):
        await client.send_message(message.channel, "GSET")

    async def help(self, client, message):
        await client.send_message(message.channel, self.name + " usage: `!gwhat`")
