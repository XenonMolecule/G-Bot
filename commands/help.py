from utils.command import Command

class Help(Command):
    def __init__(self, command_list):
        super().__init__("help")
        self.command_list = command_list
        self.command_list.append(self)
        self.command_names = [x.name for x in self.command_list]

    async def run(self, client, message, type, params):
        if(len(params) > 0):
            for name in params:
                if(name in self.command_names):
                    cmd_index = self.command_names.index(name)
                    await self.command_list[cmd_index].help(client, message)
                else:
                    await client.send_message(message.channel, "Unrecognized command: " +
                    name + "type !help for a list of commands")
        else:
            await client.send_message(message.channel, "Type ! + [command]\n\nCommand List: " +
            ", ".join(self.command_names))

    async def help(self, client, message):
        await client.send_message(message.channel, self.name + " usage: `!help`")
