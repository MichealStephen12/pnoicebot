from discord.ext import commands

class pinger(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.Cog.listener()
  async def on_message(self, message):
    channel = self.bot.get_channel(943693394637639730)


    if message.author.bot == True:
      return
    if message.content == 'n!nick submit':
      await channel.send(f"Hey! <@&870990666191208458> someones wants to change thier NNs...", delete_after = 8)
    

def setup(bot):
  bot.add_cog(pinger(bot))