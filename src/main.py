import discord
import os, json
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

    if message.content == 'Pls':
      role = get(message.guild.roles, name='beggar')
      await message.author.add_roles(role)

    if message.content.lower().contains("hi bot"):
      await message.channel.send('Hello human!')

with open(".env", encoding = 'utf-8') as f:
  try:
    env = json.loads(f.read())
    token = env["token"]
    print("Using token from env")
  except Exception as e:
    print("Failed parse env file, make sure you have a .env with valid json.")
    print("Exception:",e)

client.run(token)
