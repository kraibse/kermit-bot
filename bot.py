import discord
import config  # local module

import platform
import os

os = platform.system()

class Bot(discord.Client):
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
    bot.run(config.token)