import discord
import os
from discord.utils import get


client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is now online.'.format(client))

@client.event
async def on_message(message):
    if message.content == 'please':
      role = get(message.guild.roles, name='beggar')
      await message.author.add_roles(role)
    if message.content == 'Please':
      role = get(message.guild.roles, name='beggar')
      await message.author.add_roles(role)
    if message.content == 'pls':
      role = get(message.guild.roles, name='beggar')
      await message.author.add_roles(role)

client.run(os.getenv(".env"))
my_secret = os.environ[".env"]
