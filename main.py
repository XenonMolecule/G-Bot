import discord
import asyncio
import random
from commands.gwhat import GWhat
from commands.oobify import Oobify
from commands.altcaps import AltCaps
from commands.help import Help


from utils.commandreq import CommandRequest

from status.despacito import Despacito

CMD_CHAR = "!"
BOT_STATUS = Despacito()

command_list = []
command_names = []
rta_names = ["Apoorva", "Nick", "Brian", "Michael", "Dean Antoine", "Amy", "Rajas", "Melissa", "Siddhi", "Ryan", "Pragya"]

client = discord.Client()

def build_commands():
    global command_list
    global command_names
    command_list = [GWhat(), Oobify(), AltCaps()]
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
    await client.change_presence(game=BOT_STATUS)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(CMD_CHAR):
        req = CommandRequest(message.content)
        cmd_index = (command_names.index(req.type) if req.type in command_names else None)
        await command_list[cmd_index].run(client, message, req.type, req.params)
    if ("sad" in message.content.lower()):
        await client.send_message(message.channel, "This is so sad; Alexa play Despacito")
    if ("coke" in message.content.lower()):
        await client.send_message(message.channel, str(random.choice(rta_names)) +
        " takes the coke away.\nNo coke for you " + message.author.mention + "!")

build_commands()
client.run(get_token())
