import asyncio
from discord.ext import commands
from discord_components import Button, ButtonStyle
from controller.scum_ai import cmd
import pyperclip
from datetime import datetime
now = datetime.now()
time = now.strftime("%H:%M:%S")

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        cmd_channel = self.bot.get_channel(927796274676260944)
        if message.content.startswith('.set'):
            if message.author.guild_permissions.administrator:
                pyperclip.copy(message.content[5:])
                txt_command = pyperclip.paste()
                cmd(txt_command)
                await cmd_channel.send(f'```ini\nTime : [{time}] Name : [{member.name}] Command : [{txt_command}]\n```')
            else:
                await message.channel.send('คุณไม่ได้รับสิทธิ์ในการใช้งานคำสั่งเหล่านี้', delete_after=3)
                await asyncio.sleep(3.5)
                await message.delete()

def setup(bot):
    bot.add_cog(CommandEvents(bot))