'''
@author: kraibse

Runs the custom bot "Kermit the Frog".
'''

# import os
import platform

import discord

os = platform.system()

class Bot(discord.Client):
    '''
    Kermit discord bot class.
    Here are all the functionalities of it defined.
    '''
    token = ""
    def __init__(self):
        super().__init__() # necessary when __init__() is created
        with open("./creds.txt") as file:
            self.token = file.read()


    async def on_ready(self):
        '''
        Runs when the bot first starts up and has connected to the servers.
        '''
        # runs on first execution
        print("Logged in as '{}'".format(self.user))


    async def on_message(self, message):
        '''
        Runs when the bot reads a new message.
        '''
        # runs on message received
        print(message.content)

        if message.content == ".disconnect":
            await self.close()


if __name__ == "__main__":
    bot = Bot()
    bot.run(bot.token)
