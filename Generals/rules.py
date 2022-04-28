import discord
from  discord.ext import commands


class RuleCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  @commands.has_permissions(administrator = True)
  async def rules(self, ctx):
      embed = discord.Embed(
          title="**Rules and regulations of Pnoice hub**",
          description="disobeying rules can lead to mute and ban",
          color=discord.Colour.random()


      )
      embed.add_field(name="**Rule Number 1**", value="No spamming or flooding the chat with messages.", inline=False)
      embed.add_field(name="**Rule Number 2**", value="No text walls or a large paragraphs of text. I you are venting we have a channel for that.", inline=False)
      embed.add_field(name="**Rule Number 3**", value="No hate comments. Just respect everyone else, friendly arguments are ok.", inline=False)
      embed.add_field(name="**Rule Number 4**", value="No adult (18+), explicit, graphic content including but not limited to images, text, nicknames etc. outside of the designated NSFW room", inline=False)
      embed.add_field(name="**Rule Number 5**", value="No racist or degrading content (racial terms are allowed, but don't excessively use them).", inline=False)
      embed.add_field(name="**Rule Number 6**", value="No excessively cursing. Swearing is obviously allowed but keep it chill.", inline=False)
      embed.add_field(name="**Rule Number 7**", value="No advertising other sites/discord servers (Permission must be requested from a Staff member and must be shown apon request).", inline=False)
      embed.add_field(name="**Rule Number 8**", value="Posting your own content such as videos or photos YOU have created are allowed, just don't use it as a form of self promotion", inline=False)
      embed.add_field(name="**Rule Number 9**", value="No begging or repeatedly asking for help in the chat, just DM a staff member.", inline=False)
      embed.add_field(name="**Rule Number 10**", value="No passing off someone else's content as your own. (As a content creator I will personally ban you.)", inline=False)
      embed.add_field(name="**Rule Number 11**", value="Inviting unofficial bots is NOT ALLOWED without administrative approval.", inline=False)
      embed.add_field(name="**Rule Number 12**", value="do not mention everyone without permission from a staff member.", inline=False)
      embed.add_field(name="**Rule Number 13**", value="Do not perform or promote the intentional use of glitches, hacks, or bugs.", inline=False)
      embed.add_field(name="**Rule Number 14**", value="Do not cause a nuisance in the community, repeated complaints from several members will lead to administrative action.", inline=False)
      embed.add_field(name="**Rule Number 15**", value="Do not argue with staff. If you feel you have been wrongly treated, politely DM a staff member and ask for help.", inline=False)
      embed.set_image(url="https://media.discordapp.net/attachments/877607818436423760/919201138056769676/pnoicebanner.gif?width=603&height=339")
      await ctx.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(RuleCommand(bot))