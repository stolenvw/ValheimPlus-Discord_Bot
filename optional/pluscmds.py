import discord, typing, config
from discord.ext import commands

class Plus(commands.Cog):
    """
    Plus commands
    """

    def __init__(self, bot):
        self.bot = bot

    async def chancheck(ctx):
        if ctx.channel.id == config.LOGCHAN_ID or commands.is_owner():
            return True

    @commands.command(name='vplus',
                      brief="Plus settings",
                      help="Shows Plus mod settings. \n Available arg: enabled, disabled, section name \n Enabled: Shows enabled sections. \n Disabled: Shows disabled sections. \n Section Name: Shows settings for that section.",
                      usage="<arg>",
                      )
    @commands.has_any_role(config.VPLUS_CMD)
    @commands.check(chancheck)
    async def vplus(self, ctx, arg: typing.Optional[str] = 'help'):
        ldrembed = discord.Embed(title="Valheim Plus Settings " + arg + "", color=0x33a163)
        botsql = self.bot.get_cog('BotSQL')
        mycursor = await botsql.get_cursor()
        if arg == "help":
            ldrembed.add_field(name="{}vplus enabled".format(self.bot.command_prefix),
                                value="Shows list of enabled sections.\n Example: `{}vplus enabled`".format(self.bot.command_prefix),
                                inline=True)
            ldrembed.add_field(name="{}vplus disabled".format(self.bot.command_prefix),
                                value="Shows list of disabled sections.\n Example: `{}vplus disabled`".format(self.bot.command_prefix),
                                inline=True)
            ldrembed.add_field(name="{}vplus <section>".format(self.bot.command_prefix),
                                value="Shows setting for section.\n Example: `{}vplus Fermenter`".format(self.bot.command_prefix),
                                inline=True)
        elif arg == "enabled":
            sql = """SELECT section FROM vplus WHERE enabled = 'true' AND option1 = '0'"""
            mycursor.execute(sql)
            Info = mycursor.fetchall()
            row_count = mycursor.rowcount
            vcount = 0
            for ind in Info:
                if vcount == 1:
                    description = description + '\n' + ind[0]
                else:
                    description = ind[0]
                    vcount = 1
            ldrembed = discord.Embed(title="Valheim Plus Settings " + arg + "", description="" + description + "", color=0x33a163)
        elif arg == "disabled":
            sql = """SELECT section FROM vplus WHERE enabled = 'false' AND option1 = '0'"""
            mycursor.execute(sql)
            Info = mycursor.fetchall()
            row_count = mycursor.rowcount
            vcount = 0
            for ind in Info:
                if vcount == 1:
                    description = description + '\n' + ind[0]
                else:
                    description = ind[0]
                    vcount = 1
            ldrembed = discord.Embed(title="Valheim Plus Settings " + arg + "", description="" + description + "", color=0x33a163)
        else:
            sql = """SELECT option1, settings FROM vplus WHERE section = '%s' AND option1 != '0'""" % (arg)
            mycursor.execute(sql)
            Info = mycursor.fetchall()
            row_count = mycursor.rowcount
            for ind in Info:
                ldrembed.add_field(name="{}".format(ind[0]),
                                   value="{}".format(ind[1]),
                                   inline=False)
        mycursor.close()
        await ctx.send(embed=ldrembed)

    @vplus.error
    async def vplus_error_handler(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            if config.USEDEBUGCHAN == True:
                bugchan = self.bot.get_channel(config.BUGCHANNEL_ID)
                bugerror = discord.Embed(title=":sos: **ERROR** :sos:", description='**{}** Tried to use command: **{}**\n{}'.format(ctx.author, ctx.command, error), color=0xFF001E)
                await bugchan.send(embed=bugerror)
        if isinstance(error, commands.CheckFailure):
            if config.USEDEBUGCHAN == True:
                bugchan = self.bot.get_channel(config.BUGCHANNEL_ID)
                bugerror = discord.Embed(title=":sos: **ERROR** :sos:", description='**{}** Tried to use command: **{}**\nIn channel **#{}**'.format(ctx.author, ctx.command, ctx.channel), color=0xFF001E)
                await bugchan.send(embed=bugerror)

def setup(bot):
    bot.add_cog(Plus(bot))
