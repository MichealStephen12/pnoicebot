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

        if emoji == '💖':
          role1 = discord.utils.get(guild.roles, name = '!!𝐒𝐋𝐀𝐏𝐒𝐎𝐈𝐋')
          await member.add_roles(role1)
          await member.edit(nick = f'ƧԼƧ • {member.name}')

        if emoji == '🦋':
          role2 = discord.utils.get(guild.roles, name = 'Paro Paro G')
          await member.add_roles(role2)
          await member.edit(nick = f'PPG {member.name}')

        if emoji == '🦎':
          role3 = discord.utils.get(guild.roles, name = '!!𓆈 𝚂𝚊𝚖𝚊𝚑𝚊𝚗 𝚗𝚐 𝙱𝚊𝚢𝚊𝚠𝚊𝚔')
          await member.add_roles(role3)
          await member.edit(nick = f'𝚂𝙽𝙱︲ {member.name}')

        if emoji == '🧧':
          role4 = discord.utils.get(guild.roles, name = 'Nobility of Camaraderie')
          await member.add_roles(role4)
          await member.edit(nick = f'𝓝𝓒 - {member.name}')
        


  
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
      message = 932999255096975391
      
      if message == payload.message_id:
        guild = await(self.bot.fetch_guild(payload.guild_id))

        
        emoji = payload.emoji.name
        if emoji == '💖':
          removerole = discord.utils.get(guild.roles, name = '!!𝐒𝐋𝐀𝐏𝐒𝐎𝐈𝐋')
        if emoji == '🦋':
          removerole = discord.utils.get(guild.roles, name = 'Paro Paro G')
        if emoji == '🦎':
          removerole = discord.utils.get(guild.roles, name = '!!𓆈 𝚂𝚊𝚖𝚊𝚑𝚊𝚗 𝚗𝚐 𝙱𝚊𝚢𝚊𝚠𝚊𝚔')
        if emoji == '🧧':
          removerole = discord.utils.get(guild.roles, name = 'Nobility of Camaraderie')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
          await member.edit(nick = f'{member.name}')
          await member.remove_roles(removerole)
        else:
          print('member not found')

      
      
          
      
def setup(bot):
  bot.add_cog(NNchange(bot))