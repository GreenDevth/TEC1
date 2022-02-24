import asyncio
import random

import discord

from db.shopping_queue import Order_add, check_queue
from db.shopping_store import get_steam_id
from db.scum_events_db_ import get_location, update_status


class SnipperEventView(discord.ui.View):
    def __init__(self):
        super(SnipperEventView, self).__init__(timeout=None)

    @discord.ui.button(label='รับเซ็ต M82A1', style=discord.ButtonStyle.success, emoji='🔫', custom_id='snipper_set')
    async def snipper_set(self, button, interaction):
        member = interaction.user
        product_code = "order{}".format(random.randint(0, 999999))
        steam_id = get_steam_id(member.id)
        package_name = "snipper_set"
        # check = check_steam_exists(member.id)
        in_Order = Order_add(member.id, member.name, steam_id, product_code, package_name)
        await interaction.response.send_message(f'{in_Order}', ephemeral=True)
        cmd_channel = interaction.guild.get_channel(927796274676260944)
        queue = check_queue()
        # player_queue = checkout()
        if queue == 1:
            await asyncio.sleep(0.3)
            await cmd_channel.send('!checkout {}'.format(product_code))

    @discord.ui.button(label='ส่งตัวไปยัง Event', style=discord.ButtonStyle.danger, emoji='🚀', custom_id='teleport_players')
    async def teleport_players(self, button, interaction):
        member = interaction.user
        steam_id = get_steam_id(member.id)
        teleport_command = get_location()
        status = update_status()
        await interaction.response.send_message('{}'.format(status), ephemeral=True)
        cmd_channel = interaction.guild.get_channel(927796274676260944)
        await cmd_channel.send('.set {0} {1}'.format(teleport_command, steam_id))
        # queue = check_queue()
        # # player_queue = checkout()
        # if queue == 1:
        #     await asyncio.sleep(0.3)
        #     await cmd_channel.send('!checkout {0}'.format(product_code))
