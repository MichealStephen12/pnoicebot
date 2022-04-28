import discord
from discord.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send("the user has been banned")
        await ctx.message.delete()

    @ban.error
    async def banerror(self, ctx, error):
      if isinstance(error, commands.CommandError):
            await ctx.send("Mention someone you god damnit", delete_after = 5)
        

def setup(bot):
  bot.add_cog(BanCommand(bot))