import discord
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
        await ctx.reply(list_player, mention_author=False)
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
        await ctx.reply(count_player, mention_author=False)
        await ctx.message.delete()

    @count_players.error
    async def count_players_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            message = 'You are missing the required premission to run this command!'
        else:
            message = "Something went wrong whlie running the commands"

        await ctx.reply(message, mention_author=False)

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        btn = interaction.component.custom_id
        message = None
        if btn == 'list_players':
            list_player = listplayers()
            message = list_player.strip()
        elif btn == 'count_players':
            count_player = countplayers()
            message = count_player.strip()
        await interaction.respond(content=message)
        return

    @commands.command(name='servebutton')
    async def serverbutton_commands(self, ctx):
        await ctx.send(
            file=discord.File('./img/controller.png'),
            components=[
                [
                    Button(style=ButtonStyle.blue, label='List Players', emoji='📃', custom_id='list_players'),
                    Button(style=ButtonStyle.gray, label='Count Players', emoji='🔄', custom_id='count_players')
                ]
            ]
        )


def setup(bot):
    bot.add_cog(AdminCommand(bot))
