import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
from controller.scum_ai import listplayers, countplayers
from database.Players_db import players


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
        member = interaction.author
        btn = interaction.component.custom_id
        message = None
        if btn == 'list_players':
            list_player = listplayers()
            message = list_player.strip()
            await interaction.respond(content=message)
            return
        elif btn == 'count_players':
            count_player = countplayers()
            message = count_player.strip()
            await interaction.respond(content=message)
            return
        elif btn == 'withdraw':
            coins = players(member.id)[5]
            message = f'ถอนเงิน **{coins}**'
            await interaction.respond(
                content='จำนวนเงินที่สามารถกดได้ ต่อครั้ง\n'
                        '======================\n'
                        '   **5000**  **10000**\n'
                        '======================')

            def check(res):
                return res.author == interaction.author and res.channel == interaction.channel
            msg = await self.bot.wait_for('message', check=check)
            if msg.content == 5000:
                await interaction.channel.send(f'ถอนเงินจำนวน {msg.content}', delete_after=5)
                return
            elif msg.content == 1000:
                await interaction.channel.send(f'ถอนเงินจำนวน {msg.content}', delete_after=5)
                return
            else:
                await interaction.send('ไม่สามารถจ่ายเงินจำนวน {} ให้คุณได้'.format(msg.content), delete_after=5)
            return
        elif btn == 'balance':
            message = f'ยอดเงินทั้งหมด **{players(member.id)[5]}**'
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

    @commands.command(name='atm')
    async def atm_command(self, ctx):
        await ctx.send(
            file=discord.File('./img/atm_l1.png'),
            components=[
                [
                    Button(style=ButtonStyle.green, label='ถอนเงิน', emoji='💵', custom_id='withdraw'),
                    Button(style=ButtonStyle.blue, label='เช็คยอดเงิน', emoji='🏧', custom_id='balance')
                ]
            ]
        )


def setup(bot):
    bot.add_cog(AdminCommand(bot))
