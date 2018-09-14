import discord
import asyncio
import random
import time

import gSearch

user = 'username' #Discord Username
passw = 'password' #Discord Password

client = discord.Client()

async def birdBot():
    await client.wait_until_ready()

    bots = ['birdBot', 'dragonBot']
    botsIcon = ['🐦', '🐉']

    while not client.is_closed:
        for botId in range(0,len(bots)):

            #makes logging easier to follow
            print("----------------------------------")

            msg = "["+botsIcon[botId]+"] Bot]: "

            # Reads the bots configurations
            botConfigs = open('Profiles/'+bots[botId]+'/channels.txt', 'r')
            channels = botConfigs.readlines()
            botConfigs.close()

            # Removes \n
            for i in range(0, len(channels)):
                channels[i] = channels[i].replace("\n", '')

            botConfigs = open('Profiles/'+bots[botId]+'/tags.txt', 'r')
            tags = botConfigs.readlines()
            botConfigs.close()

            # Removes \n
            for i in range(0, len(tags)):
                tags[i] = tags[i].replace("\n", ' ')

            #makes a tag list so each search is randomised
            numberOfTags = 3
            tagsList = []
            for i in range(0, numberOfTags):
                tagsList.append(tags[random.randint(0, len(tags)-1)])

            for i in range(0, len(channels)):
                print("["+botsIcon[botId]+" Bot]: Preparing message for: ",client.get_channel(channels[i]))

                if(botsIcon[botId] == '🐦'):
                    tagsList += ['bird']
                elif(botsIcon[botId] == '🐉'):
                    tagsList += ['dragon']

                print(tagsList)

                channelName = client.get_channel(channels[i])
                urlAdd = gSearch.search(tagsList)

                #Assembles and Sends the message
                msg = "[" + botsIcon[botId] + " Bot]: Auto Message: " + urlAdd

                print(msg)
                await client.send_message(client.get_channel(channels[i]), msg)
        await asyncio.sleep(1500)

print("Initallising bots...")

client.loop.create_task(birdBot())

client.run(user, passw)