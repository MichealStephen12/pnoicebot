import discord
from discord.ext import commands

class StatusCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      client = f'<@!{self.bot.user.id}>'
      if message.content == client:
        embed = discord.Embed(title="**P-Noice Bot Commands**", description="The bot's prefix is `pn-`",  color= discord.Colour.random())
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="General Commands", value="`snipe`, `serverinfo`, `whois`, `avatar`,`confess`, `giveaway`, `profile`, `rules`, `covid`", inline=False)
        embed.add_field(name="Music Commands", value="`join`, `leave`, `music`", inline=False)
        embed.add_field(name="Game Commands", value="`ttt`, `sokoban`", inline=False)
        embed.add_field(name="Fun Commands", value="`Madlips`, `meme`", inline=False)
        embed.add_field(name="Moderation Commands", value="`kick`, `ban`, `mute`, `unmute`, `tempban`, `clear`", inline=False)
        embed.set_footer(text='\u200b requested by: {}'.format(message.author.display_name))
        await message.channel.send(embed=embed, delete_after = 10)
        return

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="**P-Noice Bot Commands**", description="The bot's prefix is `pn-`",  color= discord.Colour.random())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="General Commands", value="`snipe`, `purge`, `serverinfo`, `whois`, `avatar`,`confess`, `giveaway`, `profile`, `rules`, `covid`", inline=False)
        embed.add_field(name="Music Commands", value="`join`, `leave`, `music`", inline=False)
        embed.add_field(name="Game Commands", value="`ttt`, `sokoban`", inline=False)
        embed.add_field(name="Fun Commands", value="`Madlips`, `meme`", inline=False)
        embed.add_field(name="Moderation Commands", value="`kick`, `ban`, `mute`, `unmute`, `tempban`, `clear`", inline=False)
        embed.set_footer(text='\u200b requested by: {}'.format(ctx.author.display_name))
        await ctx.channel.send(embed=embed, delete_after = 10)


def setup(bot):
    bot.add_cog(StatusCommand(bot))