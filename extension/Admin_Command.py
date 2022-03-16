import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
from controller.scum_ai import listplayers, countplayers, cmd
from database.Players_db import players, update_coins

from mysql.connector import MySQLConnection, Error
from database.db_config import read_db_config

db = read_db_config()


def players_info(discord_id):
    try:
        conn = MySQLConnection(**db)
        cur = conn.cursor()
        cur.execute('SELECT * FROM scum_players WHERE DISCORD_ID = %s', (discord_id,))
        row = cur.fetchone()
        while row is not None:
            for x in row:
                return x
        return
    except Error as e:
        print(e)


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
            check = players_info(member.id)
            if check is not None:
                coins = players(member.id)[5]
                message = f'ถอนเงิน **{coins}**'
                await interaction.respond(
                    file=discord.File('./img/bank.png'),
                    components=[
                        [
                            Button(style=ButtonStyle.green, label='$5000', emoji='💵', custom_id='b5000'),
                            Button(style=ButtonStyle.blue, label='$10000', emoji='💵', custom_id='b10000')
                        ]
                    ]
                )
                return
            elif check is None:
                await interaction.respond(content='ไม่พบข้อมูลผู้ใช้งานในระบบ')
                return
            return

        elif btn == 'b5000':
            check = players_info(member.id)
            if check is not None:
                coins = players(member.id)[5]
                steam_id = players(member.id)[3]
                pay = 5000
                if pay < coins:
                    await interaction.respond(content='กรุณารับธนบัตร หลังจากได้รับข้อความจากระบบ')
                    cmd("#SpawnItem BP_Cash 1 location {}".format(steam_id))
                    total = coins - pay
                    current_coins = update_coins(member.id, total)
                    await discord.DMChannel.send(member, f'คุณได้ถอนเงินจำนวน **{pay}** ยอดเงินคงเหลือ **{current_coins}**')
                    return
                elif coins < pay:
                    await interaction.respond(content='ขออภัยยอดเงินในบัญชีของคุณไม่เพียงพอ')
                return
            elif check is None:
                await interaction.respond(content='ไม่พบข้อมูลผู้ใช้งานในระบบ')
                return
            return
        elif btn == 'b10000':
            check = players_info(member.id)
            if check is not None:
                coins = players(member.id)[5]
                steam_id = players(member.id)[3]
                pay = 10000
                if pay < coins:
                    await interaction.respond(content='กรุณารับธนบัตร หลังจากได้รับข้อความจากระบบ')
                    cmd("#SpawnItem BP_Cash 2 location {}".format(steam_id))
                    total = coins - pay
                    current_coins = update_coins(member.id, total)
                    await discord.DMChannel.send(member, f'คุณได้ถอนเงินจำนวน **{pay}** ยอดเงินคงเหลือ **{current_coins}**')
                    return
                elif coins < pay:
                    await interaction.respond(content='ขออภัยยอดเงินในบัญชีของคุณไม่เพียงพอ')
                return
            elif check is None:
                await interaction.respond(content='ไม่พบข้อมูลผู้ใช้งานในระบบ')
                return
            return

            # def check(res): return res.author == interaction.author and res.channel == interaction.channel msg =
            # await self.bot.wait_for('message', check=check) message = msg.content if message == 5000: if message <
            # coins: await interaction.channel.send(f'คุณถอนเงินจำนวน {message}', delete_after=5) return elif coins <
            # message: await interaction.channel.send('ขออภัยยอดเงินของคุณไม่เพียงพอสำหรับการทำรายการนี้',
            # delete_after=5) return return elif message == 10000: if message < coins: await
            # interaction.channel.send(f'คุณถอนเงินจำนวน {message}', delete_after=5) return elif coins < message:
            # await interaction.channel.send('ขออภัยยอดเงินของคุณไม่เพียงพอสำหรับการทำรายการนี้', delete_after=5)
            # return return

        elif btn == 'balance':
            check = players_info(member.id)
            if check is not None:
                message = f'ยอดเงินทั้งหมด **{players(member.id)[5]}**'
                await interaction.respond(content=message)
                return
            elif check is None:
                await interaction.respond(content='ไม่พบข้อมูลผู้ใช้งานในระบบ')
                return
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
