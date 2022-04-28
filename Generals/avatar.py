import discord
from discord.ext import commands

class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["av"])
    @commands.has_permissions(attach_files = True)
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
      if avamember == None:
        avamember = ctx.author
        
      
      embed = discord.Embed(title = f"{avamember.name}'s Avatar", color=discord.Colour.random())
      embed.set_image(url=avamember.avatar_url)
        
      await ctx.send(embed=embed, delete_after = 10)
      await ctx.message.delete()


    @avatar.error
    async def errors(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send((f'sorri pre {ctx.author.mention} pero need mo muna mag grind HUEHUEHUE'), delete_after = 7)


def setup(bot):
  bot.add_cog(AvatarCommand(bot))