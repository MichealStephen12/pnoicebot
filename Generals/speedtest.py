import discord
import speedtest
from discord.ext import commands


class Sokoban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases = ['st'])
    async def speed(ctx):

        embed = discord.Embed(description="loading speedtest")
        var = await ctx.send(embed = embed)
    

        s = speedtest.Speedtest()
        down = s.download() * 0.000001
        up = s.upload() * 0.000001
        await var.delete()
        embed2 = discord.Embed(description= f"result\n download speed = {down}\n upload speed = {up}")
        rint(down)
        print(up)
        await ctx.send(embed = embed2, delete_after = 5)


def setup(bot):
  bot.add_cog(Sokoban(bot))