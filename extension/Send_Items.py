from discord.ext import commands
from database.Store_db import get_spawner_code
from controller.scum_ai import cmd
import time
from database.Players_db import players_info


class SendItem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sendpack')
    @commands.has_permissions(manage_roles=True)
    async def send_pack_command(self, ctx, arg: str, arg2: str):
        member = players_info(ctx.author.id)
        steam_id = players_info(arg2)
        package = get_spawner_code(arg)
        spawn_code = package.split(",")
        for x in spawn_code:
            time.sleep(0.5)
            cmd("{} location {}".format(x, steam_id))
        await ctx.send(f"```ini\n[{self.bot.name}] send [{arg}] to [{steam_id}]\n```")

    @send_pack_command.error
    async def send_pack_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply('Only for Admin')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Missing a required argument :{}'.format(error.param))


def setup(bot):
    bot.add_cog(SendItem(bot))
