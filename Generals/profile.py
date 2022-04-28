import discord
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont

def circle (pfp, size = (215,215)):
  pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

  bigsize = (pfp.size[0] * 3, pfp.size[1]* 3)
  mask = Image.new('L', bigsize, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0,0) + bigsize, fill=255)
  mask = mask.resize(pfp.size, Image.ANTIALIAS)
  mask = ImageChops.darker(mask, pfp.split()[-1])
  pfp.putalpha(mask)
  return pfp



class ProfileYEAH(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def profile(self, ctx, member: discord.Member = None):
    if not member:
      member = ctx.author


    name = member.name
    
    created_at = member.created_at.strftime("%a %b %Y")

    joined_at= member.joined_at.strftime("%a %b %Y")

    base = Image.open("P-Noice.png").convert("RGBA")

    pfp = member.avatar_url_as(size = 256)
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")

    name = f"{name[:16]}.." if len(name)> 16 else name

    draw = ImageDraw.Draw(base)
    pfp = circle(pfp,(380,380))
    font = ImageFont.truetype("Nunito-Regular.ttf", 40)
    subfont = ImageFont.truetype("Nunito-Regular.ttf", 40)
    
    draw.text((150,142),name,font=font, fill=(0,0,0,255))
    draw.text((170,275),joined_at,font=subfont, fill=(0,0,0,255))
    draw.text((190,410),created_at,font=subfont, fill=(0,0,0,255))
    base.paste(pfp,(585,130),pfp)


    with BytesIO() as a:
      base.save(a,"PNG")
      a.seek(0)
      await ctx.send(file = discord.File(a,"profile.png"))

def setup(bot):
  bot.add_cog(ProfileYEAH(bot))