import urllib.request
import urllib.parse
import random
import discord
import time
import asyncio

# Discord backend login info
user = ####Discord Username
passw = ####Discord Password
botName = ""
botTag = "#"

# Key words for parsing
flags = ['-p']

# Other files that contain python code
import goodVsEvil

print("Connecting to discord server with cridentials...")
client = discord.Client()

@client.event
async def on_ready():
    botName = client.user.name
    print("Connected as: ", botName, "Using the tag: "+botTag+client.user.name[:1])
    avalon.botInit()
    print("Init. bot complete!")

# Reads/parses messages
@client.event
async def on_message(message):
    # Assigns tags to use for the bot
    bot = botTag+client.user.name[:1]
    messageContents = message.content.split(" ")

    # If the bot tag is within the message, do the following operations...
    if(botTag in message.content):
        startTime = time.time() # Used to calculate the time between commands

        # Makes sure that the message is within the AvalonBot server, check the following within the message...
        if(int(message.server.id) == int(513058363685470210)):
            print("---------------------------------------") # Makes logging the terminal outputs easier to read
            print("Got message within avalon server: Author: "+ message.author.name + " ; Message: " + message.content)

            # Checks if a message contains a flag
            for word in messageContents:

                # If '-p' is within the message, request to start a game
                if(word == flags[0]):
                    print("Sending request to data controler")
                    avalon.dataController(message.author.id, message.author.name, message.channel.id, flags[0])

                    # Checks to see if the channel already has a game
                    await client.send_message(message.channel, "Ayby")
        
        # Calculates the time between commands
        endTime = time.time()
        print("Request took:", endTime-startTime,"s")


client.run(user, passw)
