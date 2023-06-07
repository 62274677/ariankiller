import os
import discord
#import json
import yaml
import re
from logging import Logger


import time
import datetime
import traceback



# cursor.execute("CREATE TABLE user(discord_handle, username, password)")
# cursor.execute

# driver = initiate_driver()


    
 

# client = discord.Client(intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())
prefix = 'z!'

def emote(guild, name):
    return discord.utils.get(guild.emojis, name=name)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    embed.timestamp = datetime.datetime.utcnow()
    await client.send(embed=embed)
    
@client.event   
async def on_message(message):
    # print(message.content)
    if 'public_thread' in message.channel.type.name:
        if inlist(message.channel.name,storage['blocklist']['channel']['thread']):
            if inlist(message.author.id, storage['user']['blocked']):
                await message.delete()
            # if message.author 
# print(os.listdir("/git_repo"))
# print(os.listdir("/git_repo/data"))
def inlist(value,input_list):
    if isinstance(input_list,list):
        for item in input_list:
            for key,val in item.items():
                if val == value or value == key:
                    return True
    elif isinstance(input_list,dict):
        for key,val in input_list.items():
                if val == value or value == key:
                    return True
    return False
token = yaml.full_load(open('token.yaml'))['token']
storage = yaml.full_load(open('storage.yaml'))
   
client.run(token)
