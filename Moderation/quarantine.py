import discord
from discord.ext import commands



class TempbanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(aliases=["q"])
    @commands.has_permissions(kick_members=True)
    async def quarantine(self, ctx, member: discord.Member):
        role = ctx.guild.get_role(874737893132881950)

        if role in member.roles:
          await ctx.send(f"the user is already tempbanned",  delete_after = 10)
          return

        await member.edit(roles=[role]) # Replaces all current roles with roles in list
        await ctx.send((member.mention)+' has been tempbanned!', delete_after = 5)
          

    @quarantine.error
    async def muteerror(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permission", delete_after = 10) 
            return
        if isinstance(error, commands.BadArgument):
            await ctx.send("That is not a valid member", delete_after = 10)
        if isinstance(error, commands.CommandError):
            await ctx.send("Mention someone you god damnit", delete_after = 5)



    @commands.command(aliases=["uq"])
    @commands.has_permissions(kick_members=True)
    async def unquarantine(self, ctx, member: discord.Member):
        
        role = ctx.guild.get_role(874737893132881950)

        if role not in member.roles:
          await ctx.send(f"the user is not temporary banned",  delete_after = 10)
          return
        
      
        await member.remove_roles(role)
        await member.send(f" you have unquarantined from: - {ctx.guild.name}")
        await ctx.send(f"Successfully unquarantined {member.mention}", delete_after = 5)
        await ctx.message.delete()
          

    @unquarantine.error
    async def unmuteerror(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permission", delete_after = 10) 
            return
        if isinstance(error, commands.BadArgument):
            await ctx.send("That is not a valid member", delete_after = 10)
        if isinstance(error, commands.CommandError):
            await ctx.send("Mention someone you god damnit", delete_after = 5)


def setup(bot):
  bot.add_cog(TempbanCommand(bot))