import discord
from discord.ext import commands


class NNchange(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
      message = 932999255096975391
    
      if message == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == 'π':
          role1 = discord.utils.get(guild.roles, name = '!!ππππππππ')
          await member.add_roles(role1)
          await member.edit(nick = f'Ζ§ΤΌΖ§ β’ {member.name}')

        if emoji == 'π¦':
          role2 = discord.utils.get(guild.roles, name = 'Paro Paro G')
          await member.add_roles(role2)
          await member.edit(nick = f'PPG {member.name}')

        if emoji == 'π¦':
          role3 = discord.utils.get(guild.roles, name = '!!π πππππππ ππ π±ππ’ππ ππ')
          await member.add_roles(role3)
          await member.edit(nick = f'ππ½π±οΈ² {member.name}')

        if emoji == 'π§§':
          role4 = discord.utils.get(guild.roles, name = 'Nobility of Camaraderie')
          await member.add_roles(role4)
          await member.edit(nick = f'ππ - {member.name}')
        


  
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
      message = 932999255096975391
      
      if message == payload.message_id:
        guild = await(self.bot.fetch_guild(payload.guild_id))

        
        emoji = payload.emoji.name
        if emoji == 'π':
          removerole = discord.utils.get(guild.roles, name = '!!ππππππππ')
        if emoji == 'π¦':
          removerole = discord.utils.get(guild.roles, name = 'Paro Paro G')
        if emoji == 'π¦':
          removerole = discord.utils.get(guild.roles, name = '!!π πππππππ ππ π±ππ’ππ ππ')
        if emoji == 'π§§':
          removerole = discord.utils.get(guild.roles, name = 'Nobility of Camaraderie')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
          await member.edit(nick = f'{member.name}')
          await member.remove_roles(removerole)
        else:
          print('member not found')

      
      
          
      
def setup(bot):
  bot.add_cog(NNchange(bot))