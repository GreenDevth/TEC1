import asyncio
import time
from datetime import datetime

from discord.ext import commands

from controller.scum_ai import cmd, get_location
from database.Store import *

now = datetime.now()
times = now.strftime("%H:%M:%S")


class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        cmd_channel = self.bot.get_channel(927796274676260944)
        location_command = self.bot.get_channel(948477565251780658)
        if message.content.startswith('.set'):
            if message.author.guild_permissions.administrator:
                msg = message.content[5:]
                cmd(msg)
                await cmd_channel.send(f'```ini\nTime : [{times}] Name : [{member.name}] Command : [{msg}]\n```')
            else:
                await message.channel.send('คุณไม่ได้รับสิทธิ์ในการใช้งานคำสั่งเหล่านี้', delete_after=3)
                await asyncio.sleep(3.5)
                await message.delete()
        elif message.content.startswith('.location'):
            msg = message.content[10:]
            result = get_location(msg)
            await location_command.send(f'```{result}```')
        elif message.content.startswith('!checkout'):
            if message.author.guild_permissions.administrator:
                msg = message.content[10:]
                data = get_queue(msg)
                steam_id = data[0]
                package = get_package(data[1])
                spawn_code = package.split(",")
                count = check_queue()
                while True:
                    if count != 0:
                        time.sleep(1)
                        for x in spawn_code:
                            time.sleep(0.5)
                            cmd("{} location {}".format(x, steam_id))
                            await cmd_channel.send(
                                f'```ini\nTime : [{times}] Command : [{x} Location {steam_id}]\n```'
                            )
                        delete_row()
                        time.sleep(1)
                        message = f'current queue is {count}'

                    else:
                        message = f'Delivery end number of queue is {count}'
                        break
                        # await message.channel.send('คิวในการส่งของตอนนี้ เหลือ {} คิว'.format(count))
                    print(message)
                    return
        elif message.content.startswith('--run'):
            cmd_command_channel = self.bot.get_channel(925559937323659274)
            if message.author.guild_permissions.administrator:
                msg = message.content[6:]
                # data = get_queue(msg)
                # steam_id = data[0]
                # package = get_package(data[1])
                # spawn_code = package.split(",")

                while True:
                    count = check_queue()
                    if count != 0:
                        data = get_queue()
                        steam_id = data[0]
                        package = get_package(data[1])
                        spawn_code = package.split(",")
                        time.sleep(1)
                        for x in spawn_code:
                            time.sleep(1)
                            cmd("{} location {}".format(x, steam_id))
                            await cmd_channel.send(
                                f'```ini\nName : [TEC1] Command : [{x} Location {steam_id}]\n```'
                            )
                        delete_row()
                        message = f'คำสั่งซื้อคงเหลือ {count}'
                        print(message)
                        await cmd_channel.send(f'```ini\n[{message}]\n```')
                        await cmd_command_channel.send('คำสั่งซื้อหมายเลข {} จัดส่งสินค้าเสร็จสิ้น'.format(msg))
                        time.sleep(1)
                    else:
                        break
                await cmd_command_channel.send('จัดส่งสินค้าเสร็จสิ้น')
                message = 'จัดส่งสินค้าเสร็จสิ้น'
                print(message)
                return


def setup(bot):
    bot.add_cog(CommandEvents(bot))
