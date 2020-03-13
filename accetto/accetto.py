import discord
from discord.ext import commands

class accetto(commands.Cog):
      def __init__(self, bot):
            self.bot = bot

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$testù'):
            await message.channel.send('testù')

def setup(bot):
      bot.add_cog(accetto(bot))
