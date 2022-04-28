import discord
from discord.ext import commands

class PurgingCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, limit: int):
          await ctx.channel.purge(limit=limit)
          await ctx.send('Cleared by {}'.format(ctx.author.mention), delete_after = 3)
          await ctx.message.delete()
          return

  @clear.error
  async def clear_error1(self, ctx, error):

      if isinstance(error, commands.MissingPermissions):
          await ctx.send(f'Hey {ctx.author.mention} you have missing permission to execute this command')
          return
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send(f'use pn-purge <number> to clear hideous messages.')

def setup(bot):
  bot.add_cog(PurgingCommand(bot))