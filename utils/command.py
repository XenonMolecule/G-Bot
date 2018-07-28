from abc import ABC, abstractmethod

class Command(object):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    async def run(self, client, message, type, params):
        pass

    # Send message providing help
    @abstractmethod
    async def help(self, client, message):
        pass

    async def error(self, client, message, output):
        await client.send_message(message.channel, "Error in Command: " + self.name +
        "\n" + output + "\n Try !help " + name + "for information on how to use this command")
