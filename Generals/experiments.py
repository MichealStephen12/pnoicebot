import discord
from discord.ext import commands
from discord.utils import get

class sticky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # @commands.Cog.listener()
    # async def on_message(self, message):

    #   channel1 = self.bot.get_channel(928495373113229342)

    #   if message.author.bot == True:
    #     return

    #   if channel1 == message.channel:
    #     await channel1.send(message.content)

    # @commands.command()
    # async def stick(self, ctx):
    #   d = await ctx.send('what do you want to stick?')
    #   await ctx.message.delete()
    #   def check(m):
    #     return m.author.id == ctx.author.id
    #   channel = self.bot.get_channel(927859885926907934)

      

    #   message = await self.bot.wait_for('message', check = check)
    #   await message.delete()
    #   await d.delete()
      
        
    #   await channel.send(message.content)
      

def setup(bot):
  bot.add_cog(sticky(bot))