import discord
from discord.ext import commands
import asyncio

class ConfessCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confess(self ,ctx):
      if ctx.channel.type == discord.ChannelType.private:
        embed = discord.Embed(title = "type your confession")
        embed.set_footer(text = 'by DaWAE ')
        demand = await ctx.send(embed = embed)

        try:
            msg = await self.bot.wait_for('message', timeout = 150, check = lambda message: message.author == ctx.author and message.channel == ctx.channel)
            print(f"{ctx.message.author} confessed {msg.content}")

            channel1 = (self.bot.get_channel(871795017457500171))
            await channel1.send(f"{ctx.message.author} confessed {msg.content}")
            
            # with open('Confessionlogs.txt.txt', 'a') as f:
            #     f.write(f"\n\n{ctx.message.author} confessed {msg.content}")

            if msg:
              channel = (self.bot.get_channel(856755109148753920))
              embed = discord.Embed(title = f"Confession", description = f"{msg.content}")
              embed2 = discord.Embed(title = 'confession sent...')
              embed.set_footer(text="Do confessions on my dms only")
              await ctx.author.send(embed = embed2)
              await channel.send(embed = embed)

        
        except asyncio.TimeoutError:
          await ctx.send('took too long for you to confess and it crashed', delete_after = 5)
          await demand.delete()
      
      else:
        await ctx.send('i only accept confessions through dms')

    

def setup(bot):
  bot.add_cog(ConfessCommand(bot))