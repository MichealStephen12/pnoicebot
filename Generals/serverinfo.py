import discord
from discord.ext import commands

class ServerinfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, aliases =['server'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="Server Info",colour=discord.Colour.random())
        embed.add_field(name="Server Name:", value=ctx.message.guild.name, inline = True)
        embed.add_field(name="Members:", value=ctx.guild.member_count)
        embed.add_field(name="Highest Role:", value=ctx.author.top_role.mention)
        embed.add_field(name="Channels:", value=len(ctx.message.guild.channels))
        embed.add_field(name="Requested:", value=str(ctx.message.author.mention))
        embed.set_footer(text = 'by Da Wae')
        await ctx.send(embed=embed, delete_after = 10)
        await ctx.message.delete()


def setup(bot):
  bot.add_cog(ServerinfoCommand(bot))