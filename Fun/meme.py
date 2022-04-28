import discord
import json
import urllib
from discord.ext import commands



class Memes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def meme(self, ctx):
    memeApi = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")

    memeData = json.load(memeApi)

    memeUrl = memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed = discord.Embed(title = memeName)
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"meme by: {memePoster} | Subredddit: {memeSub} | Post: {memeLink}")
    await ctx.send(embed = embed, delete_after = 15)
    await ctx.message.delete()


def setup(bot):
  bot.add_cog(Memes(bot))