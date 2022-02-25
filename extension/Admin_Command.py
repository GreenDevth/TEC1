from discord.ext import commands
from discord_components import Button, ButtonStyle
from controller.scum_ai import listplayers, countplayers


class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="players")
    @commands.has_permissions(manage_roles=True)
    async def players_list(self, ctx):
        list_player = listplayers()
        await ctx.reply(list_player)
        await ctx.message.delete()

    @players_list.error
    async def players_list_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            message = 'You are missing the required premission to run this command!'
        else:
            message = "Something went wrong whlie running the commands"

        await ctx.reply(message, mention_author=False)

    @commands.command(name='count_players')
    @commands.has_permissions(manage_roles=True)
    async def count_players(self, ctx):
        count_player = countplayers()
        await ctx.reply(count_player)
        await ctx.message.delete()

    @count_players.error
    async def count_players_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            message = 'You are missing the required premission to run this command!'
        else:
            message = "Something went wrong whlie running the commands"

        await ctx.reply(message, mention_author=False)


def setup(bot):
    bot.add_cog(AdminCommand(bot))
