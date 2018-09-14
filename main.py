import urllib.request
import urllib.parse
import random
import discord
import time
import asyncio

#web search bots
import gSearch
import ySearch

user = "username"#Discord Username
passw = "password"#Discord Password
botName = ""
botTag = "#"

flags = ['-w','-e','-g','-y']

print("Connecting to discord server with cridentials...")

client = discord.Client()

@client.event
async def on_ready():
    botName = client.user.name
    print("Connected as: ", botName, "Using the tag: "+botTag+client.user.name[:1])

    print("Connecting bots...")
    import autoBot


@client.event
async def on_message(message):
    #print(message.content) #For Debug

    #Assigns tags to use for the bot
    bot = botTag+client.user.name[:1]
    messageContents = message.content.split(" ")

    #requests for the help document
    if(botTag in message.content):

        startTime = time.time()

        # seperates each on_message task with a space for easier logging
        print("----------------------------------")

        for word in messageContents:
            if(word == flags[0]):
                msg = "[Wiki Bot]: "
                url = 'https://en.wikipedia.org/wiki/'

                tagStart = message.content.find("[")
                tagEnd = message.content.find("]")

                tags = message.content[tagStart + 1:tagEnd].split()
                print("[Wiki Bot]: Request from: " + message.author.name + " for tags: ")
                print(tags)

                urlAdd = "_".join(tags)
                url += urlAdd

                print(url)
                await client.send_message(message.channel, msg+url)

            elif(word == flags[2]):
                msg = "[Google Bot]: "

                tagStart = message.content.find("[")
                tagEnd = message.content.find("]")

                tags = message.content[tagStart + 1:tagEnd].split()
                print("[Google Bot]: Request from: " + message.author.name + " for tags: ")
                print(tags)

                msg += gSearch.search(tags)
                await client.send_message(message.channel, msg)

            elif (word == flags[3]):
                msg = "[📹 Bot]: "

                tagStart = message.content.find("[")
                tagEnd = message.content.find("]")

                tags = message.content[tagStart + 1:tagEnd].split()
                print("[📹 Bot]: Request from: " + message.author.name + " for tags: ")
                print(tags)

                msg += ySearch.search(tags)
                await client.send_message(message.channel, msg)


        endTime = time.time()

        print("Request took:", endTime-startTime,"s")


client.run(user, passw)