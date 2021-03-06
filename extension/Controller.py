import asyncio

import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
from controller.scum_ai import start_game, login_game, goto_home, fixed_lost, check_screen


class ScumController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name} is online")
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(type=discord.ActivityType.playing, name='SCUM')
        )

    @commands.command(name='start')
    async def start_game_controller(self, ctx):
        game_start = start_game()
        await ctx.reply(f'{game_start}', mention_author=False)

    @commands.command(name='login')
    async def login_game_controller(self, ctx):
        game_login = login_game()
        await ctx.reply(f'{game_login}', mention_author=False)

    @commands.command(name='lost')
    async def lost_game_controller(self, ctx):
        game_lost = fixed_lost()
        message = str(game_lost)
        await ctx.reply(f'{message}', mention_author=False)

    @commands.command(name='home')
    async def home_game_controller(self, ctx):
        game_home = goto_home()
        await ctx.reply(f'{game_home}', mention_author=False)

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        btn = interaction.component.custom_id
        message = None
        if btn == 'game_start':
            game_start = start_game()
            message = str(game_start)
            await interaction.respond(content="กำลังเปิดโปรแกรมเกมส์")
            await interaction.channel.send(content=f'{message}', delete_after=5)
            return

        elif btn == 'game_login':
            game_login = login_game()
            message = str(game_login)
            await interaction.respond(content=f'กำลังทำการล็อคอินเข้าเซิร์ฟเวอร์')
            await interaction.channel.send(content=f'{message}', delete_after=5)
            return

        elif btn == 'goto_home':
            game_home = goto_home()
            message = str(game_home)
            await interaction.respond(content=f'ระบบกำลังส่งโดรนไปประจำตำแหน่ง')
            await interaction.channel.send(content=f'{message}', delete_after=5)
            return

        elif btn == 'lost':
            print(f'{btn}')
            game_lost = fixed_lost()
            message = str(game_lost)
            await interaction.respond(content=f'ระบบกับแก้ปัญหาการหลุดออกจากเกมส์ของโดรน')
            await interaction.channel.send(content=f'{message}', delete_after=5)
            return
        elif btn == 'check_drone':
            await interaction.respond(content="โปรดรอสักครู่ บอทกำลังตรวจสอบสถานะโดรนส่งของให้คุณ")
            check_screen()
            await asyncio.sleep(2)
            await interaction.channel.send(
                "โปรดสังเกตุที่รูปเพื่อพิจารณาว่า โดรนกำลังออนไลน์อยู่หรือไม่",
                file=discord.File('check_1.png'), delete_after=10
            )

    @commands.command(name='controller')
    async def scum_controller(self, ctx):
        await ctx.send(
            file=discord.File('./img/controller.png'),
            components=[
                [
                    Button(style=ButtonStyle.red, label='START', custom_id='game_start', emoji='🎮'),
                    Button(style=ButtonStyle.gray, label='LOGIN', custom_id='game_login', emoji='🔐'),
                    Button(style=ButtonStyle.green, label='HOME', custom_id='goto_home', emoji='🏡'),
                    Button(style=ButtonStyle.blue, label='LOST', custom_id='lost', emoji='🌏')
                ]
            ]
        )

    @commands.command(name="check_drone")
    async def check_drone(self, ctx):
        await ctx.send(
            components=[Button(style=ButtonStyle.red, label="CHECK DRONE", emoji='📷', custom_id='check_drone')]
        )
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ScumController(bot))
