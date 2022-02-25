import time
import atexit
from discord.ext import commands
from discord_components import DiscordComponents
from database.Auth import get_token, load_cog
# from apscheduler.schedulers.background import BackgroundScheduler
# from database.Store import check_queue



# def check_order():
#     count = check_queue()
#     if count != 0:
#         print('spawn item now')

# scheduler = BackgroundScheduler()
# job = scheduler.add_job(check_order, trigger='interval', seconds=3)

# scheduler.start()

# atexit.register(lambda: scheduler.shutdown())



token = get_token(5)
bot = commands.Bot(command_prefix='>>')
DiscordComponents(bot)


load_cog(bot)
bot.run(token)
