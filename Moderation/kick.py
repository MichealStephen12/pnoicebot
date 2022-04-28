import discord
from discord.ext import commands

class KickCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
          reason = "no reason provided"
        await ctx.guild.kick(member)
        await ctx.send(f'User {member.mention} has been kicked for being {reason}')

    @kick.error
    async def clear_error2(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'Hey {ctx.author.mention} have missing permission to execute this command')


def setup(bot):
  bot.add_cog(KickCommands(bot))