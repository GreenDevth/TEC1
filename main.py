from discord.ext import commands
from discord_components import DiscordComponents

from database.Auth import get_token, load_cog

token = get_token(5)
bot = commands.Bot(command_prefix='>>')
DiscordComponents(bot)


load_cog(bot)
bot.run(token)
