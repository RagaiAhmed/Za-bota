import discord
from discord.ext import tasks
import os
import random

token = os.getenv("DiscordBot")
client = discord.Client()

Ta3zeeb = ["la1.mp3", "la2.mp3", "la3.mp3", "la4.mp3"]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    print("message received")
    isBoss = discord.utils.get(message.author.roles, name="admin")

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! I am Za-Bota, will be under the command of \'admins\'')
        await message.channel.send('I have automated drones, Wanna see some "drone" parts in my office ? ;)')

    if message.content.startswith('!catch'):
        if isBoss:
            await message.channel.send('Woah trying my best boss, I can also offer other services if you wish ;)')
        else:
            await message.channel.send('Woah you ain\'t my boss !!')

    if message.content.startswith('!detain'):
        if isBoss:
            await message.channel.send('Woah trying my best boss, I can also offer other services if you wish ;)')
        else:
            await message.channel.send('Woah you ain\'t my boss !!')

    if message.content.startswith('!come'):
        if isBoss:
            await message.channel.send('I am coming.. UwU')
            await torture(message.author, message.author.voice)
        else:
            await message.channel.send('Woah you ain\'t my boss !!')

    if message.content.startswith('!beg'):
        await message.channel.send('pls bal')
        # await message.channel.send('yes')


local_random = random.Random()


@client.event
async def on_voice_state_update(member, before, after):
    # Check if a desired channel
    if after.channel and after.channel.name == "الامن الوطني" and member.id != client.user.id:
        await torture(member, after)


async def torture(member, after):
    is_connected = any((i.id == client.user.id) for i in after.channel.members)

    # Connect if not connected to the user channel
    if not is_connected:
        voice = discord.utils.get(client.voice_clients, guild=member.guild)

        # If connected to another voice then disconnect
        if voice is not None:
            await voice.disconnect()

        await after.channel.connect()
        print("Entered voice xDD")

    # Get voice client object
    voice = discord.utils.get(client.voice_clients, guild=member.guild)

    # Check if not playing
    if not voice.is_playing():
        voice.play(discord.FFmpegPCMAudio(local_random.choice(Ta3zeeb)))  # Play random ta3zeeb
        print("Playing torture sounds :3")

    # Unmute self
    for m in after.channel.members:
        if m.id == client.user.id:
            await m.edit(mute=False)


target_channel_id = 868655289891700816


@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = client.get_channel(target_channel_id)
    print(f"Daily spanking initiated :p {message_channel}")
    await message_channel.send("pls spank <@367668673583906817>")


client.run(token)
