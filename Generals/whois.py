import discord
from discord.ext import commands


class WhoisCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author

        embed = discord.Embed(colour=discord.Colour.random(), timestamp=ctx.message.created_at,title=f"{member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id, inline = False)
        embed.add_field(name="Server Name:", value=member.display_name,  inline = False)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)

        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline = False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
  bot.add_cog(WhoisCommand(bot))