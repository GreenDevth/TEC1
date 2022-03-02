import asyncio
import time
from datetime import datetime

from discord.ext import commands

from controller.scum_ai import cmd
from database.Store import check_queue, get_queue, get_package, delete_row

now = datetime.now()
times = now.strftime("%H:%M:%S")


class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        cmd_channel = self.bot.get_channel(927796274676260944)
        if message.content.startswith('.set'):
            if message.author.guild_permissions.administrator:
                msg = message.content[5:]
                cmd(msg)
                await cmd_channel.send(f'```ini\nTime : [{times}] Name : [{member.name}] Command : [{msg}]\n```')
            else:
                await message.channel.send('คุณไม่ได้รับสิทธิ์ในการใช้งานคำสั่งเหล่านี้', delete_after=3)
                await asyncio.sleep(3.5)
                await message.delete()
        elif message.content.startswith('!checkout'):
            if message.author.guild_permissions.administrator:
                msg = message.content[10:]
                data = get_queue(msg)
                steam_id = data[0]
                package = get_package(data[1])
                spawn_code = package.split(",")
                count = check_queue()
                while True:
                    if count != 0 or count == 1:
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


def setup(bot):
    bot.add_cog(CommandEvents(bot))
