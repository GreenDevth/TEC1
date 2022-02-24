from abc import ABC
import discord
from discord.ext import commands
from views.game_controller import GamcontrollerView
from views.snipper_event import SnipperEventView
from views.store_controller import StoreControllerView
from views.bot_status import BotStatusView


class ScumGameClient(commands.Bot, ABC):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(">>"))
        self.scum_game_view_added = False

    async def on_ready(self):
        if not self.scum_game_view_added:
            self.add_view(GamcontrollerView())
            self.add_view(SnipperEventView())
            self.add_view(StoreControllerView())
            self.add_view(BotStatusView())
            self.scum_game_view_added = True
            print(f'Logged in as {self.user.name}')
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='SCUM'))