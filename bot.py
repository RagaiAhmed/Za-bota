import discord
import os

token = os.getenv("DiscordBot")
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print("message received")

    if message.content.startswith('!Hello'):
        await message.channel.send('Hello! I am Za-Bota, will be under the command of the Minister Of Interior :D')
        await message.channel.send('I have automated drones, Wanna see some "drone" parts in my office ? ;)')

    if message.content.startswith('!Catch '):
        await message.channel.send('Woah you ain\'t my boss !!')

client.run(token)
