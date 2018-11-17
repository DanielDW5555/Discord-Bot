import discord

# List of game objects
gameInstantObjects = []

# List of chat rooms with the avalon game enabled
gameChannelList = [513065591423107072]

# List of game rooms and people within the rooms
gameRoomPlayers = [[]] # Creates a 2d array of players that are in each game room

# Class for game instances
class gameInstance():
    def gameIsFull():
        if(len(listOfPlayers) > 1):
            return True

    def __init__(self):
        listOfPlayers = []

# Class for player data
#class player:
 #   def __init__(self, playerId, playerName, alignment)

# Takes in user request and figures out what game to request
def dataController(playerId, playerName, channelId, request):
    print("Data recieved: " + str(playerId) + " " + str(playerName) + " " + str(channelId) + " " + str(request))
    
    # game room 1 in avalon discord
    for currentGameChannel in gameChannelList:
        if(int(channelId) == int(currentGameChannel)):
            if(gameInstantObjects[0].gameIsFull()):
                print("game in progress")
            else:
                gameInstantObjects[0].listOfPlayers.append(playerId)
                print(gameInstantObjects[0].listOfPlayers)

def botInit():
    game1 = gameInstance()
    gameInstantObjects.append(game1)
    game1.gameIsFull()