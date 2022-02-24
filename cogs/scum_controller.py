import asyncio
import time

import discord
import pyautogui as ai
import pyperclip
from discord.ext import commands
# import pygetwindow as gw
import pandas as pd
from db.scum_players import get_steam_id
from views.game_controller import GamcontrollerView
from views.snipper_event import SnipperEventView
from views.store_controller import StoreControllerView
from views.bot_status import BotStatusView
from pack.package import get_pack
from db.shopping_store import delete_row, get_package, get_queue
from db.shopping_queue import check_queue


def cmd(tex_commands):
    time.sleep(0.5)
    icon = './img/login.PNG'
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.click(scum)
    ai.write(tex_commands)
    time.sleep(0.1)
    ai.press('enter')

# def spawnitem(txt_command):
#     time.sleep(0.5)
#     icon = './img/login.PNG'
#     scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
#     ai.click(scum)
#     data = get_queue(txt_command)
#     steam_id = data[0]
#     pack = data[1]
#     package = get_package(pack)
#     package_cmd = package.split(",")
#     while True:
#         count = check_queue()
#         if count != 0:
#             time.sleep(0.1)
#             for x in package_cmd:
#                 time.sleep(0.5)
#                 ai.write(f'{x} location {steam_id}')
#                 time.sleep(0.5)
#             delete_row()

def cmds():
    time.sleep(0.5)
    icon = './img/login.PNG'
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.click(scum)
    ai.write('#listplayers true')
    time.sleep(0.1)
    ai.press('enter')


def location(text):
    time.sleep(0.5)
    icon = './img/login.PNG'
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.click(scum)
    ai.write(f'#Location {text} true')
    time.sleep(0.1)
    ai.press('enter')


class GameControllerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='game_controller')
    @commands.is_owner()
    # Run Controller for Game Controller
    async def event_controller(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send(file=discord.File('./img/controller.png'), view=GamcontrollerView())

    @commands.Cog.listener()
    # """Admin Commands for run SCUM COMMAND"""
    async def on_message(self, message):

        cm_channel = self.bot.get_channel(927796274676260944)
        if message.content.startswith('.set'):
            if message.channel.id == cm_channel.id:
                pyperclip.copy(message.content[5:])
                text_commands = pyperclip.paste()
                cmd_channel = self.bot.get_channel(927796274676260944)
                await cmd_channel.send(text_commands)
                cmd(text_commands)
            else:
                await message.channel.send('คุณไม่ได้รับสิทธิ์ในการใช้งานคำสั่งนี้', delete_after=3)

        if message.content.startswith('!checkout'):
            cmd_channel = self.bot.get_channel(927796274676260944)
            if message.channel.id == cmd_channel.id:
                msg = message.content[10:]
                data = get_queue(msg)
                steam_id = data[0]
                pack = data[1]
                package = get_package(pack)
                package_cmd = package.split(",")
                while True:
                    count = check_queue()
                    if count != 0:
                        time.sleep(0.1)
                        for x in package_cmd:
                            time.sleep(0.5)
                            cmd("{} location {}".format(x, steam_id))
                            await message.channel.send('{}'.format(x))

                        delete_row()
                        time.sleep(2)
                        await message.channel.send('คิวในการส่งของตอนนี้ เหลือ {} คิว'.format(count))

                    else:
                        await message.channel.send('คิวในการส่งของตอนนี้ เหลือ {} คิว'.format(count))
                        return

    @commands.command(name='get_pack')
    @commands.has_role('Admin')
    # Commands For Get Entry pack in database.
    async def get_pack(self, ctx, *, arg):
        member = ctx.author
        steam_id = get_steam_id(member.id)
        send_pack = get_pack(arg)
        res = send_pack.split(",")
        await ctx.message.delete()
        await asyncio.sleep(0.1)
        for x in res:
            time.sleep(0.1)
            cmd("{} location {}".format(x, steam_id))
        await ctx.send('package mk18 send to {} successfully.'.format(steam_id))


    @commands.command(name='get')
    async def get_command(self, ctx, *, arg):
        location(arg)
        txt = pyperclip.paste()
        await ctx.reply(f'```{txt}\n```')

    @commands.command(name="players")
    async def players_list(self, ctx):
        await ctx.message.delete()
        cmds()
        txt = pyperclip.paste()
        df = pd.read_clipboard(txt)
        index = df.index
        number_of_rows = len(index) - 1
        text = df.to_string(index=False)

        await asyncio.sleep(1)
        await ctx.send(f'```{text}\n\n'
                               f'==================================================\nTotal {number_of_rows} player and 1 Drone```')

    @commands.command(name='count_players')
    async def count_players(self, ctx):
        await ctx.message.delete()
        cmds()
        txt = pyperclip.paste()
        df = pd.read_clipboard(txt)
        index = df.index
        number_of_rows = len(index) - 1
        text = df.to_string()
        await asyncio.sleep(1)
        await ctx.channel.send(f'ขณะนี้มีผู้เล่นออนไลน์ ทั้งหมด **{number_of_rows}** คน บอท 1 ตัว')

    @commands.command(name='snipper_event')
    @commands.is_owner()
    async def snipper_event(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send(file=discord.File('./img/snipper_set.png'), view=SnipperEventView())

    @commands.command(name='reset_store')
    @commands.is_owner()
    async def reset_store(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send(file=discord.File('./img/controller.png'), view=StoreControllerView())

    @commands.command(name='robot_status')
    async def robot_status(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send(
            '**เช็คสถานะการทำงานของบอท**\n\nบอทส่งของอาจจะมีบางครั้งที่สัญญาณเน็ตมีปัญหาและทำให้บอทหลุดออกจากเซิร์ฟ '
            'ดังนั้นเพื่อให้การส่งของสำเร็จ '
            'ผู้เล่นต้องเช็คสถานะของบอทโดยกดที่ปุ่มด้านล่างเพื่อเช็คว่าบอทกำลังออนไลน์อยู่หรือไม่ '
            'หากมีการตอบกลับจากระบบแสดงว่าบอทกำลังออนไลน์ แต่หากไม่มีการตอบกลับจากระบบแสดงว่า '
            'บอทหลุดออกจากเซิร์ฟไปแล้ว',
            file=discord.File('./img/line.png'))
        await ctx.channel.send(file=discord.File('./img/drone.png'), view=BotStatusView())
