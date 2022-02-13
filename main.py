import discord

import random as rand
import os
import praw
import requests
import json




from discord.ext import commands
from PIL import Image

from replit import db
client = discord.Client()

poem=["https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/1.jpg" ,"https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/2.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/3.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/4.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/5.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/6.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/7.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/8.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/9.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/10.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/11.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/12.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/14.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/15.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/16.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/17.jpg","https://raw.githubusercontent.com/scan-vidhaan/poemsss/main/18.jpg" ]


disp=rand.choice(poem)















@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
  

    if msg.startswith('$poem'):

        await message.channel.send(rand.choice(poem))
        
    if msg.startswith('$hi'):

     await message.channel.send("Hi i am vidhaan the dude who loves you the most.\n Use $poem command to start off :)")
       
 

   
       
    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

   


client.run('OTQwMjM3NzQzMDk3Nzc0MDkw.YgEeog.uOBpAML5EgnAIBfencteWa6DYxA')