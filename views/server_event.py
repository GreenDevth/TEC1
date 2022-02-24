import discord


class ServerEventView(discord.ui.View):
    def __init__(self):
        super(ServerEventView, self).__init__(timeout=None)