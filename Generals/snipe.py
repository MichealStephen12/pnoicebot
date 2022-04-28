import discord
from discord.ext import commands
from asyncio import sleep

class SnipeCommand(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      self.snipe_message_author = {}
      self.snipe_message_authorID = {}
      self.snipe_message_content = {}
      self.snipe_message_time = {}
      self.snipe_message_pfp = {}

  @commands.Cog.listener()
  async def on_message_delete(self, message):
      if message.author.bot == False:
          self.snipe_message_authorID[message.channel.id] = message.author.id
          self.snipe_message_author[message.channel.id] = message.author
          self.snipe_message_content[message.channel.id] = message.content
          hours = message.created_at.strftime("%H")
          fHours = int(hours) - 4
          current_timezone_time = message.created_at.strftime(str(fHours) + ":" + "%M" + " %p")
          self.snipe_message_time[message.channel.id] = current_timezone_time
          self.snipe_message_pfp[message.channel.id] = message.author.avatar_url

          await sleep(60)
          del self.snipe_message_author[message.channel.id]
          del self.snipe_message_content[message.channel.id]
          del self.snipe_message_time[message.channel.id]
          del self.snipe_message_pfp[message.channel.id]

  @commands.command(name = 'snipe')
  async def snipe(self, ctx):
      channel = ctx.channel
      try:
          em = discord.Embed(description = self.snipe_message_content[channel.id], color=discord.Color.random(), )
          em.set_footer(text = str(f"Last deleted message in {channel.name} Today at " + self.snipe_message_time[channel.id]))
          em.set_author(name=self.snipe_message_author[channel.id], icon_url=self.snipe_message_pfp[channel.id])
          await ctx.send(embed = em)
      except:
          await ctx.send(f"There are no recently deleted messages by in #{channel.mention}")

def setup(bot):
  bot.add_cog(SnipeCommand(bot))

