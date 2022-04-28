import discord
from discord.ext import commands

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member):
        role = ctx.guild.get_role(857292970226221066)
        owner = ctx.guild.get_role(870694613172781106)
        ginoo = ctx.guild.get_role(946089233481871360)
        botself = ctx.guild.get_role(898118549237792790)

        if ginoo in member.roles:
          await ctx.send(f"beach you cant mute this motherfather, this folks are higher than you idiot.", delete_after = 10)
          await ctx.message.delete()
          return

        if owner in member.roles:
          await ctx.send(f"bro seriously? muting someone with an owner role? come on dawg that ain't in discord policy you stupid matherfather.",  delete_after = 10)
          await ctx.message.delete()
          return
        
        if botself in member.roles:
          await ctx.send(f"YOU'RE MUTING ME??? if only i weren't a bot boi",  delete_after = 10)
          await ctx.message.delete()
          return

        if role in member.roles:
          await ctx.send(f"the user is already muted BRO EASY STOP BEING A SAVAGE",  delete_after = 5)
          await ctx.message.delete()
          return

        else:
          await member.add_roles(role) 
          await member.send(f" you have muted from: - {ctx.guild.name}")
          await ctx.send(f"This piece of sheet is Successfully muted {member.mention} know where you belong TRASH", delete_after = 5)
          await ctx.message.delete()

    @mute.error
    async def mute_error2(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("you dont have the permission to use thanos power boi", delete_after = 5) 
            return
        if isinstance(error, commands.BadArgument):
            await ctx.send("what the faq is this? this aint a creature to be muted.", delete_after = 5)
            return
        if isinstance(error, commands.CommandError):
            await ctx.send("Mention someone you god damnit", delete_after = 5)



    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
      role = ctx.guild.get_role(857292970226221066)
      owner = ctx.guild.get_role(870694613172781106)
      ginoo = ctx.guild.get_role(946089233481871360)
      botself = ctx.guild.get_role(898118549237792790)

      if ginoo in member.roles:
        await ctx.send(f"beach first of all, this motherfather is already unmuted and not being muted, 2nd of all stop wasting my time, 3rd of all i don't care about your opinion, and for the love of god this role can't muted bro please.", delete_after = 10)
        await ctx.message.delete()
        return

      if owner in member.roles:
        await ctx.send(f"BROOOO this guy has an owner role WTF ARE YOU THINKING? oh and btw this role cant be muted okay? put it in your memory core you saggy assed nerd.", delete_after = 10)
        await ctx.message.delete()
        return
      
      if botself in member.roles:
          await ctx.send(f"YOU'RE MUTING ME??? if only i weren't a bot boi",  delete_after = 10)
          await ctx.message.delete()
          return


      if role not in member.roles:
          await ctx.send(f"the user is already unmuted or not being muted PLEASE CHECK HIS/HER PROFILE ON THE ROLES BELOW!!! uughh",  delete_after = 5)
          await ctx.message.delete()
          return

      await member.remove_roles(mutedRole)
      await member.send(f" you have unmutedd from: - {ctx.guild.name}")
      await ctx.send(f"awwwww lucky ass is already Successfully unmuted {member.mention} what a lucky bastard", delete_after = 5)
      await ctx.message.delete()


    @unmute.error
    async def mute_error1(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("ask thanos for permission boi", delete_after = 5) 
            return
        if isinstance(error, commands.BadArgument):
            await ctx.send("WHAT IS THIS? make sure you don't have an illness called TYPO SYNDROM", delete_after = 5)
            return
        if isinstance(error, commands.CommandError):
            await ctx.send("WHERES THE PERSON? SHOULD I MUTE RANDOM PEOPLE NOW?", delete_after = 5)
        


def setup(bot):
    bot.add_cog(MuteCommand(bot))