import discord
import asyncio
from commands.gwhat import GWhat
from commands.oobify import Oobify
from commands.help import Help
from utils.commandreq import CommandRequest

CMD_CHAR = "!"

command_list = []
command_names = []

client = discord.Client()

def build_commands():
    global command_list
    global command_names
    command_list = [GWhat(), Oobify()]
    help_cmd = Help(command_list)
    command_list.append(help_cmd)
    command_names = [x.name for x in command_list]

def get_token():
    token_file = open("private/token.txt")
    token = token_file.readline()[:-1]
    token_file.close()
    return token

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(CMD_CHAR):
        req = CommandRequest(message.content)
        cmd_index = (command_names.index(req.type) if req.type in command_names else None)
        await command_list[cmd_index].run(client, message, req.type, req.params)

build_commands()
client.run(get_token())
