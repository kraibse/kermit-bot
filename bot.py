import discord
import config  # local module

import platform
import os

os = platform.system()

class Bot(discord.Client):
    token = ""
    def __init__(self):
        # reads the token from token.txt
        with open("/etc/share/kermit-token.txt") as file:
            self.token = file.read()


    async def on_ready(self):
        # runs on first execution
        print("Logged in as '{}'".format(self.user))


    async def on_message(self, message):
        # runs on message received
        print(message.content)

        if message.content == ".disconnect":
            await self.close()


if __name__ == "__main__":
    bot = Bot()
    bot.run(bot.token)